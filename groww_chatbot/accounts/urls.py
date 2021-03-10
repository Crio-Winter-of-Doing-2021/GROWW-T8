from django.urls import path,include
from . import views

urlpatterns = [
    path('api/<int:pk>/', views.ProfileView.as_view(), name='profile-view'),
    path('<int:id>/',views.ProfileDetailView.as_view() ,name='profile-detail-view'),
]