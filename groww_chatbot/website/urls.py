from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.loginuser,name='login'),
    path('logout/',views.logoutuser, name='logout'),
    path('register/',views.registeruser, name='register'),
    path('explore/<str:type>/',views.ProductListView.as_view(), name='product-list-view'),
    path('explore/<str:type>/<str:name>/',views.ProductDetailsView.as_view(), name='product-details'),
    path('api/<str:type>/',views.ProductList.as_view(), name='product_list'),
    path('api/<str:type>/<str:name>/',views.ProductDetails.as_view(), name='product-details')
]