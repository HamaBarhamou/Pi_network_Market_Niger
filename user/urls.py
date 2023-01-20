from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name="login"),
    path('logout', views.deconnexion, name='logout'),
    path('register', views.register, name='register')
]