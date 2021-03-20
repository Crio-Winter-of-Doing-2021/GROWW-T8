from django.urls import path,include
from .views import ChatterBotApiView
from .views import ChatterBotAppView
from . import views

urlpatterns = [
    path('', ChatterBotAppView.as_view(), name='main'),
    path('api/chatterbot/',ChatterBotApiView.as_view(), name='chatterbot'),
    path('random/',views.random,name='random')
]

