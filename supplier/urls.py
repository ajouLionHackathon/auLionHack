from django.contrib import admin
from django.urls import path
from . import views

app_name='supplier'# 여기서 앱네임은 나중에 name 할때 다른 앱이랑 겹칠까봐 네임스페이스 역할을 해주는 겁니다.

urlpatterns = [
    path('',views.show_drawings,name='show_drawings'),

]
