from django import forms
from django.forms import ModelForm
from django.db import models
from .models import Category, Shop, Article
from user.models import User


class ShopForm(ModelForm):
    class Meta:
        model = Shop
        exclude = ('user', 'market')
        #ields = '__all__'


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        exclude = ('shop',)

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        exclude = ('vendeur','views_count')
        
    def __init__(self, *args, **kwargs):
        #user = kwargs.pop('user')
        super(ArticleForm, self).__init__(*args, **kwargs)
