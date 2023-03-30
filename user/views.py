from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, LoginForm
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect
from shop.models import Shop


# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib import messages



from django.contrib.auth.forms import AuthenticationForm

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error(None, "Invalid login credentials. Please try again.")
        else:
            form.add_error(None, "Invalid login credentials. Please try again.")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})




def deconnexion(request):
    logout(request)
    form = LoginForm()
    context = {'form': form}
    return redirect('/')


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
            return redirect('/')
    else:
        form = UserRegisterForm()

    context = {'form': form} # Ajouter le formulaire dans le contexte

    if form.errors:
        context['errors'] = form.errors # Ajouter les erreurs de validation dans le contexte

    return render(request, 'registration/register.html', context)



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            # Add error message if authentication fails
            return render(request, 'registration/login.html', {'error': 'Invalid credentials'})
    return render(request, 'registration/login.html')

