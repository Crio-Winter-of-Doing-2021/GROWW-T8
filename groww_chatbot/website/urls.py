from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.loginuser,name='login'),
    path('logout/',views.logoutuser, name='logout'),
    path('register/',views.registeruser, name='register')
]