from django import forms
from .models import Jasoseol

class JssForm(forms.ModelForm):
    class Meta:
        model = Jasoseol
        # 만들고 싶은 field
        fields = ('title', 'content',)