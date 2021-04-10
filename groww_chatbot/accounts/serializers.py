from .models import Profile
from django.db.models import fields
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		exclude = ['user',"timestamp"]