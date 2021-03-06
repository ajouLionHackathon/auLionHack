from django import forms
# from django.contrib.auth import get_user_model
from account.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        # models = get_user_model()
        model = User
        fields = UserCreationForm.Meta.fields+('phone','sex','nickname','name','age','address',)

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)