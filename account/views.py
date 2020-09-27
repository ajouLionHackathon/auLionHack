from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate as auth_authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import CustomUserCreationForm,LoginForm


# Create your views here.

def signup(request):
    if request.method=="POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return render(request,'account/loginhome.html')
        else:
            return HttpResponse('회원가입이 실패했습니다.')
    else:
        form = CustomUserCreationForm()
        return render(request, 'account/signup.html',{'form':form})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth_authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return render(request,'account/loginhome.html')
        else:
            return HttpResponse('로그인이 실패했습니다.')
    else:
        form = LoginForm()
        return render(request, 'account/login.html',{'form':form})
        
    

def logout(request):
    auth_logout(request)
    form = LoginForm(request.POST)
    return render(request,'account/loginhome.html',{'form':form})

def loginhome(request):
    return render(request,'account/loginhome.html')
