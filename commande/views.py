from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from panier.models import Cart
from .models import Order, OrderItem
from .forms import OrderForm



@login_required
def order_create(request):
    cart = request.session.get('cart')
    if not cart:
        return redirect('panier:cart_detail')
    
    cart = Cart.objects.get(id=cart['cart_id'])
    total_amount = sum(item.article.price * item.qte for item in cart.cartitem_set.all())
    order = Order(user=request.user, cart=cart, total_amount=total_amount)
    order.save()
    request.session['order_id'] = order.id
    
    return redirect('commande:order_confirmation')


@login_required
def order_confirmation(request):
    order_id = request.session.get('order_id')
    if not order_id:
        return redirect('panier:cart_detail')
    order = get_object_or_404(Order, id=order_id, user=request.user)
    context = {'order': order}
    return render(request, 'order_confirmation.html', context)

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    items = OrderItem.objects.filter(order=order)
    context = {'order': order, 'items': items}
    return render(request, 'order_detail.html', context)

@login_required
def order_cancel(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if order.status != 'pending':
        return redirect('commande:order_detail', order_id=order.id)
    if request.method == 'POST':
        order.status = 'cancelled'
        order.save()
        return redirect('commande:order_detail', order_id=order.id)
    context = {'order': order}
    return render(request, 'commande/order_cancel.html', context)

@login_required
def order_confirm(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if order.status != 'pending':
        return redirect('commande:order_detail', order_id=order.id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            order.status = 'confirmed'
            order.save()
            # Vide le panier
            #Cart.objects.filter(user=request.user).delete()
            return redirect('commande:order_detail', order_id=order.id)
    else:
        form = OrderForm(instance=order)
    context = {'order': order, 'form': form}
    return render(request, 'order_confirm.html', context)

@login_required
def order_ship(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if order.status != 'confirmed':
        return redirect('commande:order_detail', order_id=order.id)
    if request.method == 'POST':
        order.status = 'shipped'
        order.save()
        return redirect('commande:order_detail', order_id=order.id)
    context = {'order': order}
    return render(request, 'order_ship.html', context)

@login_required
def order_deliver(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if order.status != 'shipped':
        return redirect('commande:order_detail', order_id=order.id)
    if request.method == 'POST':
        order.status = 'delivered'
        order.save()
        return redirect('commande:order_detail', order_id=order.id)
    return render(request, 'order_deliver.html', {'order': order})
