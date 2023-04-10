from django.urls import path
from . import views

app_name = 'commande'

urlpatterns = [
    path('order_confirmation/', views.order_confirmation, name='order_confirmation'),
    path('order_detail/<int:order_id>/', views.order_detail, name='order_detail'),
    path('order_cancel/<int:order_id>/', views.order_cancel, name='order_cancel'),
    path('order_confirm/<int:order_id>/', views.order_confirm, name='order_confirm'),
    path('order_ship/<int:order_id>/', views.order_ship, name='order_ship'),
    path('order_deliver/<int:order_id>/', views.order_deliver, name='order_deliver'),
    path('order_create/', views.order_create, name='order_create'),
    path('history/', views.order_history, name='order_history'),
    path('tracking/<int:order_id>/', views.order_tracking, name='order_tracking'),
]
