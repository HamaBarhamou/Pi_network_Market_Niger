from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, LoginForm
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect
from shop.models import Shop


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


from django.contrib.auth import get_user_model, login, authenticate
from django.shortcuts import render, redirect
from .forms import UserRegisterForm


User = get_user_model()


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Add error message if authentication fails
            return render(request, 'registration/login.html', {'error': 'Invalid credentials'})
    return render(request, 'registration/login.html')

