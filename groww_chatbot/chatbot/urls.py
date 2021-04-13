from django.urls import path,include
from .views import ChatterBotApiView
from .views import ChatterBotAppView, ResetDatabase
from . import views

urlpatterns = [
    path('', ChatterBotAppView.as_view(), name='main'),
    path('api/chatterbot/',ChatterBotApiView.as_view(), name='chatterbot'),
    path('api/chatterbot/train',ChatterBotApiView.as_view(), name='chatterbot-train'),
    path('random/',views.random,name='random'),
    path('reset-db/',ResetDatabase.as_view(), name='reset-db'),
    path('admin/', views.AdminView.as_view() ,name='admin-view'),
    path('api/get-data/', views.GetData.as_view() ,name='get-data'),

]

