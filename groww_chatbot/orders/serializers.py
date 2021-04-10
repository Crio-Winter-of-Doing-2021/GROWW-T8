from django.db.models import fields
from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		exclude = ['category']

class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		exclude = ['profile']