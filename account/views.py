from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm

# Create your views here.
def signup(request):
    form = CustomUserCreationForm(request.POST)
    if request.method=="POST":
        if form.is_valid():
            user = form.save()
            return render(request,'mainpage/mainpage.html')
    return render(request, 'account/signup.html',{'form':form})

def login(request):
    return render(request, 'account/login.html')