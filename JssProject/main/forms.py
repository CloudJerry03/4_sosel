from django import forms
from .models import Jasoseol

class JssForm(forms.ModelForm):
    class Meta:
        model = Jasoseol
        # 만들고 싶은 field
        fields = ('title', 'content',)
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #라벨 바꾸기
        self.fields['title'].label = "제목" 
        self.fields['content'].label = "내용"
        #class, placeholder바꾸기
        self.fields['title'].widget.attrs.update({
            'class':'jss_title',#input의 class 설정
            'placeholder':'제목',
        })
        self.fields['content'].widget.attrs.update({
            'class':'jss_content',#input의 class 설정
            'placeholder':'자유롭게 자기소개서를 입력해주세요',
        })