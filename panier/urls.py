from django.urls import path
from . import views

app_name = 'panier'

urlpatterns = [
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:article_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:cart_item_id>/', views.cart_remove, name='cart_remove'),
    path('cart/update/<int:cart_item_id>/', views.cart_update, name='cart_update'),
]
