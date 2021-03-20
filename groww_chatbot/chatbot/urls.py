from django.urls import path,include
from .views import ChatterBotView
from .views import ChatterBotAppView
from . import views

urlpatterns = [
    path('', ChatterBotAppView.as_view(), name='main'),
    path('api/chatterbot/',ChatterBotView.as_view(), name='chatterbot'),
    path('random/',views.random,name='random')
]

