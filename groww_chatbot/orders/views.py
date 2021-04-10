from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from rest_framework import generics, permissions, serializers
from .serializers import OrderSerializer
from .models import Order
from accounts.models import Profile

# Create your views here.
class OrderList(generics.ListCreateAPIView):
	serializer_class = OrderSerializer
	
	def get_queryset(self):
		profile_obj = Profile.objects.get(user=self.request.user)
		return Order.objects.filter(profile=profile_obj)

class OrderListView(View):
	def get(self,request):
		return render(request,'orders/order_list.html')

class OrderDetails(generics.RetrieveAPIView):
	serializer_class = OrderSerializer
	
	def get_queryset(self):
		profile_obj = Profile.objects.get(user=self.request.user)
		return Order.objects.filter(profile=profile_obj)

class OrderDetailsView(View):
	def get(self,request,id):
		return render(request,'orders/order_details.html',{'id':id})
