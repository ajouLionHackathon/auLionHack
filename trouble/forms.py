from .models import Tr_Comment

class TrCommentForm(forms.ModelForm):
    
    class Meta:
        model = Tr_Comment
        fields = ['body']