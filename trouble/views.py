from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Trouble, Tr_Comment
from .forms import TroubleForm
# Create your views here.


def write_Trouble(request):
    if request.method == 'POST':
        form = TroubleForm(request.POST)
        if form.is_valid:
            trouble = form.save(commit=False)
            trouble.create_Date = timezone.now()
            trouble.save()
            # 저장 성공 후 어디로 갈건지 안 정해서 일단 전체 고민글 보기 페이지로 가게 함
            return redirect('trouble:read_Trouble')

    else:
        form = TroubleForm()
        form = {'form':form}
        return render(request, 'trouble/write_Trouble.html',form)


def read_Trouble(request):
    """고민들 보여주는 것 세부적이게 보여주는 것은 아님"""
    trouble_List = Trouble.objects.order_by('-create_Date')
    context = {'trouble_List': trouble_List}
    return render(request, 'trouble/trouble_List.html', context)


def detail_Trouble(request, trouble_id):
    # 여기서 사용한 pk 는 인수로 받아온거 또 인수는 어디서 받냐 urls.py에서 보내주는거
    trouble = get_object_or_404(Trouble, pk=trouble_id)
    context = {'trouble': trouble}
    return render(request, 'trouble/trouble_Detail.html', context)


def comment_Create(request, trouble_id):
    """
    댓글 등록
    """
    trouble = get_object_or_404(Trouble, pk=trouble_id)
    if request.method == "POST":
        trouble.tr_comment_set.create(
            body=request.POST.get('body'), create_Date=timezone.now())
    return redirect('trouble:detail_Trouble', trouble_id=trouble.id)


def comment_Update(request, trouble_id, comment_id):
    trouble = get_object_or_404(Trouble, pk=trouble_id)
    comment = get_object_or_404(Tr_Comment, pk=comment_id)
    # User.objects.get으로 username 받아와야 함
    # 기획적 측면에서 상의할 것이 있어 우선 비워둡니다.
    # if request.method == "POST":
    return redirect('trouble:detail_Trouble', trouble_id=trouble.id)


def comment_Delete(request, trouble_id, comment_id):
    trouble = get_object_or_404(Trouble, pk=trouble_id)
    comment = get_object_or_404(Tr_Comment, pk=comment_id)
    # User.objects.get으로 username 받아와야 함
    if request.method == "POST":
        # user가 만든 유저이면
        comment.delete()
    return redirect('trouble:detail_Trouble', trouble_id=trouble.id)
