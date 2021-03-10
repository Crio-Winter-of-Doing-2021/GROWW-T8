from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.OrderListView.as_view() ,name='order-list-view'),
	path('<int:id>/',views.OrderDetailsView.as_view(),name='order-details'),
	path('api/<int:pk>/',views.OrderDetails.as_view(),name='order-details'),
	path('api/orders/',views.OrderList.as_view(),name='order-list'),
]