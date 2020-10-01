from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
def showmypage(request):
    return render(request,'mypage/mypage_main.html')

