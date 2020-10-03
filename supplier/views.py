from django.shortcuts import render

# Create your views here.
def show_drawings(request):
    return render(request, 'supplier/supplier_drawing_list.html')