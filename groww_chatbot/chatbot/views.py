import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.shortcuts import render,redirect
from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# chatbot = ChatBot('Groww')

# Create a new trainer for the chatbot
# trainer = ChatterBotCorpusTrainer(chatbot)

# # Train the chatbot based on the english corpus
# trainer.train("chatterbot.corpus.english")


class ChatterBotAppView(TemplateView):
    template_name = 'chatbot/app.html'


class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    chatterbot = ChatBot(**settings.CHATTERBOT)
    trainer = ChatterBotCorpusTrainer(chatterbot)
    trainer.train("chatterbot.corpus.english")        
    trainer.train("chatterbot.corpus.english.greetings")        
    
    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.
        * The JSON data should contain a 'text' attribute.
        """
        input_data = json.loads(request.body.decode('utf-8'))

        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)

        response = self.chatterbot.get_response(input_data)

        response_data = response.serialize()

        return JsonResponse(response_data, status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.chatterbot.name
        })

def random(request):
    return render(request,'chatbot/chatbot.html')