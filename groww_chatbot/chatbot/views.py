import json
import chatterbot
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.shortcuts import render,redirect
from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from rest_framework.views import APIView
from rest_framework import permissions
import requests
from .models import FAQ,Category,CategoryMap
from orders.models import Product
from accounts.models import Profile
from rest_framework.renderers import JSONRenderer

chatterbot = ChatBot(**settings.CHATTERBOT)

def train_chatbot(q,a):
    trainer = ListTrainer(chatterbot)
    trainer.train([q,a])

class ResetDatabase(View):
    def get(self, request, *args, **kwargs):
        print('Starting Reset...')
        
        ## Add categories
        Category.objects.all().delete()
        
        categories = ['stocks','mutual-funds','gold','fd','account','orders','kyc','logged-in']
        f = 1
        for c in categories:
            obj = Category(name=c)
            obj.save()
        print('Categories Added...')

        ## Add FAQs and Mapping
        FAQ.objects.all().delete()
        count = 1
        path = '../Json Files/final.json'
        
        with open(path,'r') as f:
            data = json.load(f)
            for category, values in data.items():
                if category == 'orders' or category =='kyc':
                    f = True
                else:
                    f = False
                for question, answer in values.items():
                    if 'Unicorn ' in answer:
                        answer = answer[8:]
                        f = True
                    obj = FAQ(question=question, answer=answer)
                    obj.save()
                    
                    obj2 = CategoryMap(question=obj,category=Category.objects.get(name=category))
                    obj2.save()
                    if f:
                        obj2 = CategoryMap(question=obj,category=Category.objects.get(name='logged-in'))
                        obj2.save()
                    print('Count : {}'.format(count),end='\r')
                    count += 1
        
        print('FAQs Added...')

        ## Add data
        Product.objects.all().delete()
        categories = ['ST','MF','GO','FD']
        for c in categories:
            if c == 'GO':
                obj = Product(name='Gold',category='GO',price=100)
                obj.save()
            else:
                for i in range(1,4):
                    obj = Product(name='Demo_{}_{}'.format(c,i),category=c,price=100*i)
                    obj.save()

        print('Data Added...')
        print('Success')
        return JsonResponse({
            'success': True
        })


class ChatterBotAppView(TemplateView):
    template_name = 'chatbot/chatbot.html'

class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """
    buttons = []
    # chatterbot = ChatBot(**settings.CHATTERBOT)
    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.
        * The JSON data should contain a 'text' attribute.
        """
        input_data = json.loads(request.body.decode('utf-8'))
        path = input_data['path']
        user = input_data['user']
        print(input_data)
        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)
        
        try:
            category = path.split('/')[-2]
            print(category)
            c = Category.objects.get(name=category)
        except:
            if 'profile' in path:
                c = Category.objects.get(name='account')
            else:    
                c = None
        data = CategoryMap.objects.filter(category=c).values_list('question',flat=True) if c else None
        loggedIn = CategoryMap.objects.filter(category__name='logged-in').values_list('question',flat=True)
        buttons2 = None
        if data:
            buttons = FAQ.objects.filter(id__in=data)
        else:
            buttons = FAQ.objects.all()

        if user != "AnonymousUser" and c and c.name=='account':
            print(user)
            buttons.exclude(id__in=loggedIn)
            obj = Profile.objects.get(user__username=user)
            if not obj.kyc:
                kyc = CategoryMap.objects.filter(category__name='kyc').values_list('question',flat=True)
                buttons2 = FAQ.objects.filter(id__in=kyc).order_by('?').values_list('question',flat=True)
        
        buttons = list(buttons.order_by('?').values_list('question',flat=True)[:4])

        buttons = buttons2[:2] + buttons[:2] if buttons2 else buttons
        response = chatterbot.get_response(input_data)

        response_data = response.serialize()

        return JsonResponse({'response_data': response_data, 'buttons':buttons},  status=200)

    def get(self, request):
        """
        Return data corresponding to the current conversation.
        """
        # train(chatterbot)  
        chatterbot.storage.drop()
        trainer = ListTrainer(chatterbot)
        trainer.train(['I have a question',"I'm here to help, you can ask me anything!"])
        trainer.train(['Thanks',"I'm glad I could help &#128516;"])

        for item in FAQ.objects.all():
            trainer.train([item.question,item.answer])

        trainer =   ChatterBotCorpusTrainer(chatterbot)
        # trainer.train("chatterbot.corpus.english")        
        trainer.train("chatterbot.corpus.english.greetings") 

        return JsonResponse({
            'status': 'trained successfully'
        })


def random(request):
    return render(request,'chatbot/chatbot.html')

class AdminView(View):
	def get(self,request):
		return render(request,'accounts/faq.html')

class GetData(APIView):
    permission_classes = [permissions.AllowAny]
    renderer_classes = [JSONRenderer]
    
    def get(self, request):
        print("API Called")
        rtype = request.GET.get('rtype',1)
        category_id = request.GET.get('category_id')
        if rtype == 1 or rtype == '1':
            data = Category.objects.all().values()
            return JsonResponse({
                'categories': list(data)
            })
        elif rtype == 2 or rtype == '2':
            c = Category.objects.get(id=category_id)
            ids = list(CategoryMap.objects.filter(category=c).values_list('question__id',flat=True))
            data = FAQ.objects.filter(id__in=ids).values()
            return JsonResponse({
                'data' : list(data)
            })
    
    def post(self, request):
        try:
            question = request.POST.get('question')
            answer = request.POST.get('answer')
            isforbot = request.POST.get('isforbot')
            islogin = request.POST.get('islogin')
            category = request.POST.get('category')
            print("Post Question: ",question)
            print("POST Answer: ",answer)
            print('POST isforbot:',isforbot)
            print('POST islgin:',islogin)
            print('POST category:',category)
            obj = FAQ(question=question, answer=answer)
            obj.save()

            obj2 = Category.objects.get(id=category)
            CategoryMap(question=obj,category=obj2).save()

            # if islogin:
            #     obj2 = Category.objects.get(name='Logged In')
            #     CategoryMap(question=obj.id,category=obj2.id).save()


            # CategoryMap Part
            train_chatbot(question,answer)
            return JsonResponse({
                'success': True
            })
        except:
            return JsonResponse({
                'success': False
            })
    
    def patch(self, request):
        try:
            id = int(request.data.get('id'))
            question = request.data.get('question')
            answer = request.data.get('answer')
            print("PATCH Id",id)
            print("Qusetion",question)
            print("Answer",answer)
            obj = FAQ.objects.get(id=id)
            obj.question = question
            obj.answer = answer
            obj.save()
            return JsonResponse({
                'success': True
            })
        except:
            return JsonResponse({
                'success': False
            })
