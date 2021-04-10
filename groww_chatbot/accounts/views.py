from django.shortcuts import render
from accounts.serializers import ProfileSerializer
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .models import Profile
from django.http import HttpResponse, Http404
from django.shortcuts import render,redirect
from rest_framework import status
from django.views.generic.base import View



class ProfileView(APIView):
    permission_classes = [permissions.AllowAny]    
    def get(self,request,pk):
        try:
            person = Profile.objects.get(id=pk)
            print("The Person is: ", person)
            serializer = ProfileSerializer(person, many=False)
            return Response(serializer.data)
        except:
            raise Http404("User Not Found")        
        return Response(serializer.errors)    

    def patch(self,request,pk):
        try:
            person = Profile.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = request.data
        serializers = ProfileSerializer(person, data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self,request):
        serializer = ProfileSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ProfileDetailView(View):
    def get(self,request,id):
        return render(request, 'accounts/profile.html',{'id':id})