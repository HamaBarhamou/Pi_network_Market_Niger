from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart, CartItem
from shop.models import Article


# Create your views here.
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
    request.session['cart'] = {'cart_id': cart.id}
    return redirect('panier:cart_detail')


@login_required
def cart_remove(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
    article_name = cart_item.article.name
    cart_item.delete()
    messages.success(request, f"{article_name} a été retiré du panier.")
    return redirect('panier:cart_detail')


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
        return redirect('panier:cart_detail')
    context = {
        'cart_item': cart_item,
    }
    return render(request, 'cart/cart_update.html', context)