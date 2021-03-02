from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import  CreateUserForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

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
                form.save()
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
                messages.error(request, "Wrong username or password")
                # Username or password is incorrect
                print("Incorrect details")
                pass
        return render(request, 'website/login.html')
    
def logoutuser(request):
    logout(request)
    return redirect('home')