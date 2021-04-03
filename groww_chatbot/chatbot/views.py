import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.shortcuts import render,redirect
from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import requests
from .models import FAQs


class ChatterBotAppView(TemplateView):
    template_name = 'chatbot/chatbot.html'

# def train(chatterbot):
#     data = json.loads(open("C:\\Users\\Pranjal\\Desktop\\Crio_Last\\GROWW-T8\\groww_chatbot\\chatbot\\mutualfund.json","r").read())
#     train = []
#     for i in ["External Funds","Groww Funds"]:
#         for row in data[i]:
#             if row['answerHtml'] == None or row['answerHtml'] == "":
#                 train.append(str(row['questionTitle']))
#                 train.append(str(row['answerText']))
#             else:
#                 train.append(str(row['questionTitle']))
#                 train.append(str(row['answerText']))

#     trainer = ListTrainer(chatterbot)
#     trainer.train(train)

"""
chatterbot = ChatBot(**settings.CHATTERBOT)
data = json.loads(open("C:\\Users\\Pranjal\\Desktop\\Crio_Last\\GROWW-T8\\groww_chatbot\\chatbot\\mutualfund.json","r").read())
train = []

for i in ["External Funds","Groww Funds"]:
    for row in data[i]:
        if row['answerHtml'] == None or row['answerHtml'] == "":
            print(row['questionTitle'])    
            print(row['answerText'])
            train.append(str(row['questionTitle']))
            train.append(str(row['answerText']))
        else:
            print(row['questionTitle'])    
            print(row["answerHtml"])
            train.append(str(row['questionTitle']))
            train.append(str(row['answerText']))

trainer = ListTrainer(chatterbot)
trainer.train(train)
"""
category = ['stocks','fd','mutual-fund','gold']
class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """
    """
    Training Only Once 
    """
    buttons = []
    chatterbot = ChatBot(**settings.CHATTERBOT)
    # # train(chatterbot)
    # trainer = ChatterBotCorpusTrainer(chatterbot)
    # trainer.train("chatterbot.corpus.english")        
    # trainer.train("chatterbot.corpus.english.greetings")     

    # trainer = ListTrainer(chatterbot)
    # path = '../Json Files/final.json'
    # with open(path,'r') as f:
    #     data = json.load(f)
    #     for category, values in data.items():
    #         for question, answer in values.items():
    #             trainer.train([question,answer])

    
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
        if user == "AnonymousUser":
            if "/" in path:
                print("Home Page")
                buttons = ['Stocks','Mutual Fund','FD','GOLD','Account']
            if "stocks" in path:
                print("Stocks Page")
                buttons = ['How to invest in stocks?','My issue is not listed','Something else']
        else:
            haskyc = True
            if "/" in path:
                print("Home Page")
                buttons = ['Stocks','Mutual Fund','FD','GOLD','Account']
            if "stocks" in path:
                print("Stocks Page")
                buttons = ['How to invest in stocks?','My issue is not listed','Something else']

        response = self.chatterbot.get_response(input_data)

        response_data = response.serialize()

        return JsonResponse({'response_data': response_data, 'buttons':buttons},  status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.chatterbot.name
        })


def random(request):
    return render(request,'chatbot/chatbot.html')


"""Getting First Response Not important"""
# def get_first_response(input_statement, response_list, storage=None):
#     """
#     :param input_statement: A statement, that closely matches an input to the chat bot.
#     :type input_statement: Statement

#     :param response_list: A list of statement options to choose a response from.
#     :type response_list: list

#     :param storage: An instance of a storage adapter to allow the response selection
#                     method to access other statements if needed.
#     :type storage: StorageAdapter

#     :return: Return the first statement in the response list.
#     :rtype: Statement
#     """
#     logger = logging.getLogger(__name__)
#     logger.info('Selecting first response from list of {} options.'.format(
#         len(response_list)
#     ))
#     return response_list[0]
