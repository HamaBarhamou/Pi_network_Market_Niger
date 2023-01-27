from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm
from django.contrib import messages
from .forms import LoginForm
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect


# Create your views here.
def login_page(request):
    error = False

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
            else:
                error = True
    else:
        form = LoginForm()

    context = {
        'error': error,
        'form': form
    }

    template = loader.get_template('login.html')
    return HttpResponse(template.render(context, request))


def deconnexion(request):
    logout(request)
    form = LoginForm()
    context = {'form': form}
    template = loader.get_template('login.html')
    return HttpResponse(template.render(context, request))


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)		
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            fonction = form.cleaned_data['fonction']
            obj.fonction = int(fonction)
            obj.save()
            #print('fonction= ',obj.fonction)
            user = authenticate(username=username, password=password)
            login(request,user)	
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')				
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    template = loader.get_template('register.html')
    return HttpResponse(template.render(context, request))
