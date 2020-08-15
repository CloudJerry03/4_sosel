from django.shortcuts import render
from .forms import JssForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    jss_form = JssForm()
    return render(request, 'create.html', {'jss_form' : jss_form})