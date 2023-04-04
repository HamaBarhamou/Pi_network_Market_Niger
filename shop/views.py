from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from .models import Shop, Category, Article
from .forms import ShopForm, CategoryForm, ArticleForm
from django import forms
from user.models import User


@login_required
def vendor_dashboard(request):
    try:
        shop = Shop.objects.get(user=request.user)
    except Shop.DoesNotExist:
        # Rediriger l'utilisateur vers la page de création de boutique
        return redirect('shop:create_shop')

    category_list = Category.objects.filter(shop=shop)
    paginator = Paginator(category_list, 4) # Afficher 10 catégories par page

    page = request.GET.get('page')
    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        # Si la page n'est pas un entier, afficher la première page
        categories = paginator.page(1)
    except EmptyPage:
        # Si la page est vide, afficher la dernière page
        categories = paginator.page(paginator.num_pages)

    return render(request, 'vendor/dashboard.html', {'shop': shop, 'categories': categories})
    return render(request, 'vendor/dashboard.html', {'shop': shop, 'categories': categories, 'articles': articles})


@login_required
def vendor_articles(request):
    shop = get_object_or_404(Shop, user=request.user)
    articles = Article.objects.filter(category__shop=shop)
    return render(request, 'vendor/articles.html', {'articles': articles})

@login_required
def vendor_categories(request):
    shop = get_object_or_404(Shop, user=request.user)
    categories = Category.objects.filter(shop=shop)
    return render(request, 'vendor/categories.html', {'categories': categories})

@login_required
def create_shop(request):
    if request.method == 'POST':
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            shop = form.save(commit=False)
            shop.user = request.user
            shop.save()
            messages.success(request, 'Shop created successfully.')
            return redirect('shop:vendor_dashboard')
    else:
        form = ShopForm()
    return render(request, 'vendor/create_shop.html', {'form': form})

@login_required
def update_shop(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)
    if request.method == 'POST':
        form = ShopForm(request.POST, request.FILES, instance=shop)
        if form.is_valid():
            form.save()
            messages.success(request, 'Shop updated successfully.')
            return redirect('shop:vendor_dashboard')
    else:
        form = ShopForm(instance=shop)
    return render(request, 'vendor/update_shop.html', {'form': form, 'shop': shop})

@login_required
def delete_shop(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)
    shop.delete()
    messages.success(request, 'Shop deleted successfully.')
    return redirect('shop:vendor_dashboard')

@login_required
def create_category(request):
    shop = get_object_or_404(Shop, user=request.user)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save(commit=False)
            category.shop = shop
            category.save()
            messages.success(request, 'Category created successfully.')
            return redirect('shop:vendor_dashboard')
    else:
        form = CategoryForm()
    return render(request, 'vendor/create_category.html', {'form': form})

@login_required
def update_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully.')
            return redirect('shop:vendor_dashboard')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'vendor/update_category.html', {'form': form, 'category': category})

def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    articles = Article.objects.filter(category=category)
    context = {'category': category, 'articles': articles}
    return render(request, 'category_detail.html', context)

@login_required
def delete_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    messages.success(request, 'Category deleted successfully.')
    return redirect('shop:vendor_dashboard')

@login_required
def create_article(request):
    shop = get_object_or_404(Shop, user=request.user)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            article = form.save(commit=False)
            article.vendeur = request.user
            article.category.shop = shop
            article.save()
            messages.success(request, 'Article created successfully.')
            return redirect('shop:vendor_dashboard')
    else:
        categories = Category.objects.filter(shop=shop)
        form = ArticleForm(user=request.user)
        form.fields['category'].queryset = categories
    return render(request, 'vendor/create_article.html', {'form': form})




@login_required
def update_article(request, article_id):
    shop = get_object_or_404(Shop, user=request.user)
    article = get_object_or_404(Article, pk=article_id, category__shop=shop)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article, user=request.user)

        if form.is_valid():
            form.save()
            
            messages.success(request, 'Article updated successfully.')
            return redirect('shop:vendor_dashboard')
    else:
        #form = ArticleForm(instance=article)
        categories = Category.objects.filter(shop=shop)
        form = ArticleForm(instance=article, user=request.user)
        form.fields['category'].queryset = categories
    return render(request, 'vendor/update_article.html', {'form': form})

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {'article': article}
    return render(request, 'article_detail.html', context)

@login_required
def delete_article(request, article_id):
    shop = get_object_or_404(Shop, user=request.user)
    article = get_object_or_404(Article, pk=article_id, category__shop=shop)
    if request.method == 'POST':
        article.delete()
        messages.success(request, 'Article deleted successfully.')
        return redirect('shop:vendor_dashboard')
    return render(request, 'vendor/delete_article.html', {'article': article})


def vendeur_detail(request, pk):
    vendeur = get_object_or_404(User, pk=pk)
    articles = Article.objects.filter(vendeur=vendeur)
    paginator = Paginator(articles, 9)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    context = {'vendeur': vendeur, 'articles': articles}
    return render(request, 'vendor/vendeur_detail.html', context)


