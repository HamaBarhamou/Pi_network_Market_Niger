from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from .models import Shop, Category, Article, Cart, CartItem
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


def shop_list(request):
    shops = Shop.objects.all()
    search_query = request.GET.get('q')
    if search_query:
        shops = shops.filter(name__icontains=search_query)
    paginator = Paginator(shops, 10)  # afficher 10 boutiques par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'shop/shop_list.html', {'page_obj': page_obj, 'search_query': search_query})



@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    cart_total = sum(item.qte * item.article.price for item in cart_items)
    context = {
        'cart': cart,
        'cart_items': cart_items,
        'cart_total': cart_total,
    }
    return render(request, 'cart/cart_detail.html', context)


@login_required
def cart_add(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, article=article)
    if not created:
        cart_item.qte += 1
        cart_item.save()
    messages.success(request, f"{article.name} a été ajouté au panier.")
    return redirect('shop:cart_detail')


@login_required
def cart_remove(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
    article_name = cart_item.article.name
    cart_item.delete()
    messages.success(request, f"{article_name} a été retiré du panier.")
    return redirect('shop:cart_detail')


@login_required
def cart_update(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
    if request.method == 'POST':
        qte = request.POST.get('qte', 1)
        try:
            qte = int(qte)
        except ValueError:
            qte = 1
        if qte < 1:
            qte = 1
        cart_item.qte = qte
        cart_item.save()
        messages.success(request, f"La quantité pour {cart_item.article.name} a été mise à jour.")
        return redirect('shop:cart_detail')
    context = {
        'cart_item': cart_item,
    }
    return render(request, 'cart/cart_update.html', context)