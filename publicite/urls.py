from django.urls import path
from . import views

app_name = 'publicite'

urlpatterns = [
    path('publicites/', views.afficher_publicites, name='afficher_publicites'),
]
