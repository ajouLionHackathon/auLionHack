from django.shortcuts import render

# Create your views here.
def write_Trouble(request):
    return render(request,'trouble/write_Trouble.html')