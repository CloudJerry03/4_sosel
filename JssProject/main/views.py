from django.shortcuts import render, redirect
from .forms import JssForm
from .models import Jasoseol


# Create your views here.
def index(request):
    all_jss = Jasoseol.objects.all()
    return render(request, 'index.html', {'all_jss' : all_jss})

def create(request):
    if request.method == "POST":#POST일 경우 실행
        filed_form = JssForm(request.POST)
        if filed_form.is_valid():#유효성 검증
            filed_form.save()#object를 저장
            return redirect('index')

    jss_form = JssForm()
    return render(request, 'create.html', {'jss_form' : jss_form})