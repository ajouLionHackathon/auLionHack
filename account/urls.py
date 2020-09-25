from django.urls import path
import account.views

urlpatterns = [
    path('/signup', account.views.signup, name='signup'),
    path('/login', account.views.login, name='login'),
    #''(공백) url이 들어오면 post_list 함수를 호출한다
]
