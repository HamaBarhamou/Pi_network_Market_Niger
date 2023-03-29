from django.shortcuts import  HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .forms import ShopForm
from django.views.decorators.http import require_http_methods
from Pi_network_Market_Niger.utils import authors_vendor
from django.core.paginator import Paginator
from .models import Shop


@login_required(login_url='/user/')
@authors_vendor
def updateshop(request):
    """ if request.method == "POST":
        shop = Shop(
                user=request.user,
                market=Market.objects.first()
                )
        form = ShopForm(request.POST, request.FILES, instance=shop)
        if form.is_valid():
            form.save()
            form = ShopForm()
        else:
            form = ShopForm(request.POST)
    else:
        form = ShopForm()
    context = {'form': form}
    template = loader.get_template('newshop.html')
    return HttpResponse(template.render(context, request)) """
    
    shop = Shop.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES, instance=shop)
        if form.is_valid():
            shop = form.save()
            print('souavagag')
            return redirect('dashbord')
        else:
            print('formulaire invalid')
            form = ShopForm(instance=shop)  
    else:
        form = ShopForm(instance=shop)
    context = {'form': form}
    template = loader.get_template('newshop.html')
    return HttpResponse(template.render(context, request))

@login_required(login_url='/user/')
@authors_vendor
def dashbord(request):
    context = {'form': ''}
    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render(context, request))

@login_required(login_url='/user/')
@authors_vendor
def mesboutique(request):
    shop = Shop.objects.filter(user=request.user)
    paginator = Paginator(shop, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    template = loader.get_template('mesboutique.html')
    return HttpResponse(template.render(context, request))
