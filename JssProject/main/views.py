from django.shortcuts import render, redirect, get_object_or_404
from .forms import JssForm, CommentForm
from .models import Jasoseol, Comment
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    all_jss = Jasoseol.objects.all()
    return render(request, 'index.html', {'all_jss' : all_jss})

def my_index(request):
    my_jss = Jasoseol.objects.filter(author=request.user)
    return render(request, 'index.html', {'all_jss' : my_jss})


@login_required(login_url='/login/')#로그인이 필요한 것에 붙여주면 됨
def create(request):
    if not request.user.is_authenticated:#로그인 확인
        return redirect('login')

    if request.method == "POST":#POST일 경우 실행
        filled_form = JssForm(request.POST)
        if filled_form.is_valid():#유효성 검증
            temp_form = filled_form.save(commit=False)#저장을 지연 시킴
            temp_form.author = request.user
            temp_form.save()#object를 저장
            return redirect('index')

    jss_form = JssForm()
    return render(request, 'create.html', {'jss_form' : jss_form})

@login_required(login_url='/login/')#로그인이 필요한 것에 붙여주면 됨
def detail(request, jss_id):

    my_jss = get_object_or_404(Jasoseol, pk=jss_id)
    comment_form = CommentForm()
    return render(request, 'detail.html',{'my_jss':my_jss, 'comment_form': comment_form})

@login_required(login_url='/login/')#로그인이 필요한 것에 붙여주면 됨
def delete(request, jss_id):
    my_jss = Jasoseol.objects.get(pk=jss_id)
    #자신것만 삭제하게 함
    if request.user == my_jss.author:
        my_jss.delete()
        return redirect('index')
    #그렇지 않은 경우에 다음 실행
    raise PermissionDenied #권한 위반 시 띄우기

@login_required(login_url='/login/')#로그인이 필요한 것에 붙여주면 됨
def update(request, jss_id):
    my_jss = Jasoseol.objects.get(pk=jss_id)
    jss_form = JssForm(instance=my_jss)
    if request.method == "POST":
        updated_form = JssForm(request.POST, instance=my_jss)
        if updated_form.is_valid():
            updated_form.save()
            return redirect('index')

    return render(request, 'create.html', {'jss_form':jss_form})

def create_comment(request, jss_id):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        temp_form = comment_form.save(commit=False)
        temp_form.author = request.user
        temp_form.jasoseol = Jasoseol.objects.get(pk=jss_id)
        temp_form.save()
        return redirect('detail', jss_id)
    else:
        return redirect('detail', jss_id)

def delete_comment(request, jss_id, comment_id):
    my_comment = Comment.objects.get(pk=comment_id)
    if request.user == my_comment.author:
        my_comment.delete()
        return redirect('detail', jss_id)
    else:
        raise PermissionDenied