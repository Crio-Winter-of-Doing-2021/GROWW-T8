from django.db.models import fields
from rest_framework import serializers
from orders.models import *

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		exclude = ['category']