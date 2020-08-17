from django.shortcuts import render, redirect, get_object_or_404
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

def detail(request, jss_id):

    my_jss = get_object_or_404(Jasoseol, pk=jss_id)

    return render(request, 'detail.html',{'my_jss':my_jss})


def delete(request, jss_id):
    my_jss = Jasoseol.objects.get(pk=jss_id)
    my_jss.delete()
    return redirect('index')

def update(request, jss_id):
    my_jss = Jasoseol.objects.get(pk=jss_id)
    jss_form = JssForm(instance=my_jss)
    if request.method == "POST":
        updated_form = JssForm(request.POST, instance=my_jss)
        if updated_form.is_valid():
            updated_form.save()
            return redirect('index')

    return render(request, 'create.html', {'jss_form':jss_form})