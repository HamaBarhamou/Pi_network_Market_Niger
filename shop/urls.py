from django.urls import path
from . import views

urlpatterns = [
    path('newshop', views.newshop, name="newshop"),
]