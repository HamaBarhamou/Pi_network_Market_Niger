from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('vendor/dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
    path('vendor/create_shop/', views.create_shop, name='create_shop'),
    path('vendor/update_shop/<int:shop_id>/', views.update_shop, name='update_shop'),
    path('vendor/delete_shop/<int:shop_id>/', views.delete_shop, name='delete_shop'),
    path('vendor/create_category/', views.create_category, name='create_category'),
    path('vendor/update_category/<int:category_id>/', views.update_category, name='update_category'),
    path('vendor/delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('vendor/create_article/', views.create_article, name='create_article'),
    path('vendor/update_article/<int:article_id>/', views.update_article, name='update_article'),
    path('vendor/delete_article/<int:article_id>/', views.delete_article, name='delete_article'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('vendeur/<int:pk>/', views.vendeur_detail, name='vendeur_detail'),
]

