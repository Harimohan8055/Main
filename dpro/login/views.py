from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
# Create your views here.

def login(request):
    return render(request, 'login/index.html')


def register(request):
    #return render(request, 'register/index.html')
    form_class = register_form
    form = form_class(request.POST or None)
    if request.method == 'POST':
        form = register_form(request.POST)
        if form.is_valid():
            return HttpResponse('/thanks/')
        else:
            form=register_form()
    return render(request, 'register/index.html', {'form':form})

#def registerform(request):
