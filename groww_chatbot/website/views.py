from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from django.views.generic.base import View
from .forms import  CreateUserForm
from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.contrib import messages

from accounts.models import Profile
from orders.models import Product
from orders.serializers import ProductSerializer


# Create your views here.
def home(request):
    return render(request,'website/index.html')

def registeruser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                usr = form.save()
                Profile.objects.create(user=usr)
                messages.success(request, f'Account created for {username}')
                return redirect('login')
        
        context = {'form':form}
        return render(request, 'website/register.html', context)


def loginuser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, f"Wrong username or password")
                print("Incorrect details")
        return render(request, 'website/login.html')
    
def logoutuser(request):
    logout(request)
    return redirect('home')

class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'type'

    def get_queryset(self):
        type = self.kwargs.get(self.lookup_url_kwarg)
        d = {'stocks':'ST', 'mutual-funds':'MF', 'deposits':'FD', 'gold':'GO'}
        if type in ['stocks','mutual-funds','deposits','gold']:
            items = Product.objects.filter(category=d[type])
            return items
        else:
            raise Http404("Path does not exist")

class ProductDetails(APIView):
    permission_classes = [permissions.AllowAny]
    renderer_classes = [JSONRenderer]
    def get(self, request, type, name):
        print(type, name)
        if type not in ['stocks','mutual-funds','deposits','gold']:
            raise Http404("Path does not exist")
        item = Product.objects.get(name=name)
        print(item)
        serializer = ProductSerializer(item)
        return Response(serializer.data)

class ProductListView(View):
    def get(self, request, type):
        # type = self.kwargs.get('type')
        if type == 'stocks':
            name = 'Stocks'
        elif type == 'mutual-funds':
            name = 'Mutual Funds'
        elif type == 'deposits':
            name = 'Fixed Deposits (FD)'
        elif type == 'gold':
            name = 'Gold'
        else:
            raise Http404("Path does not exist")
        return render(request,'website/product.html',{'type':type, 'name':name})

class ProductDetailsView(View):
    def get(self, request, type, name):
        return render(request,'website/product_details.html',{'type':type, 'name':name})
