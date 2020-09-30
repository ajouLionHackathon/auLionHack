from django import forms
from .models import Tr_Comment, Trouble


class TrCommentForm(forms.ModelForm):

    class Meta:
        model = Tr_Comment
        fields = ['body']


class TroubleForm(forms.ModelForm):
    class Meta:
        model = Trouble
        fields = ['title', 'body', 'category', 'drawing_Filter']
