from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import Trouble
# Create your views here.
def write_Trouble(request):
    return render(request,'trouble/write_Trouble.html')

def read_Trouble(request):
    """고민들 보여주는 것 세부적이게 보여주는 것은 아님"""
    trouble_List=Trouble.objects.order_by('-create_Date')
    context={'trouble_List':trouble_List}
    return render(request,'trouble/trouble_List.html',context)


def detail_Trouble(request, trouble_id):
    trouble=get_object_or_404(Trouble,pk=trouble_id) #여기서 사용한 pk 는 인수로 받아온거 또 인수는 어디서 받냐 urls.py에서 보내주는거
    context={'trouble':trouble}
    return render(request,'trouble/trouble_Detail.html',context)


def comment_Create(request, trouble_id):
    """
    댓글 등록
    """
    trouble=get_object_or_404(Trouble,pk=trouble_id)
    trouble.tr_comment_set.create(body=request.POST.get('body'),create_Date=timezone.now())
    return redirect('trouble:detail_Trouble',trouble_id=trouble.id)