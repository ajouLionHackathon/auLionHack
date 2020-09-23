from django.contrib import admin
from django.urls import path
from . import views

app_name='trouble'# 여기서 앱네임은 나중에 name 할때 다른 앱이랑 겹칠까봐 네임스페이스 역할을 해주는 겁니다.

urlpatterns = [
    path('write/',views.write_Trouble,name='write'),
    path('<int:trouble_id>/',views.detail_Trouble, name='detail_Trouble'),
    path('',views.read_Trouble, name='read_Trouble'),
    path('comment/create/<int:trouble_id>/',views.comment_Create, name='comment_Create'),
]
