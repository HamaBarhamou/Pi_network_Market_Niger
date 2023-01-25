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


@login_required(login_url='/user/')
def newshop(request):
    if request.method == "POST":
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            form = ShopForm()
        else:
            form = ShopForm(request.POST)
    else:
        form = ShopForm()
    context = {'form': form}
    template = loader.get_template('newshop.html')
    return HttpResponse(template.render(context, request))

@login_required(login_url='/user/')
@authors_vendor
def dashbord(request):
    context = {'form': ''}
    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render(context, request))
