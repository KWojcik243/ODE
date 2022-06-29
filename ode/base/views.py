from distutils.log import error
import imp
from multiprocessing import context
import re
# from .onto.ontology import OwnOntology

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')
    context = {'page':page}
    return render(request, 'base/login.html', context=context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            # for i in range(dict(form.errors).get('username')):
            #     dict(form.errors).get('username')
            # errors = str(dict(form.errors).get('username')) + str(dict(form.errors).get('password1')) + str(dict(form.errors).get('password2'))
            # errors = errors.replace('<ul class="errorlist">', '')
            # errors = errors.replace('</li></ul>', '<br>')
            # errors = errors.replace('</li><li>', '<br>')
            # errors = errors.replace('None<li>', '')
            # errors = errors.replace('<li>', '')
            # print(dict(form.errors).get('password'))
            messages.error(request, form.errors)
    return render(request, 'base/login.html',{'form':form})

@login_required(login_url='login')
def home(request):
    return render(request, 'base/home.html')

def loginPagePl(request):
    page = 'login_pl'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')
    context = {'page':page}
    return render(request, 'base/login_pl.html', context=context)

# def open_file_req(request):
    
#     onto = OwnOntology("onto",onto)
#     return render(request, 'base/home.html')
#     # onto = OwnOntology("onto",onto)
#     # onto = get_ontology("file://D:\\Programowanie\\Programy\\Uczelnia\\Licencjat\\Projekt_Ontologyu_ODE\\Licencjat\\Application\\Backend\\onto").load()


