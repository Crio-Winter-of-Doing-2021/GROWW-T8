from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import  UserCreationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    return render(request,'website/index.html')

def registeruser(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form':form}
    return render(request, 'website/register.html', context)


def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Username or password is incorrect
            print("Incorrect details")
            pass
    return render(request, 'website/login.html')

def logoutuser(request):
    logout(request)
    return redirect('home')