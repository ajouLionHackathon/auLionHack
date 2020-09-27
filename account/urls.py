from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    #''(공백) url이 들어오면 post_list 함수를 호출한다
]
