# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    views.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bissaka- <bissaka-@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/01/31 20:19:53 by bissaka-          #+#    #+#              #
#    Updated: 2022/02/03 22:27:49 by bissaka-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from audioop import reverse
from curses.ascii import NUL
from re import template
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,Http404
from .models import Categories,Articles
from django.views import View
from django.views.generic import ListView
from .forms import NousContacter
from django.core.paginator import Paginator
# Create your views here

def ft_NousContacter(request):
    if request.method == 'POST':
        form = NousContacter(request.POST)
        if form.is_valid():
            # traitement des donne du formulaire et redirection
            return HttpResponseRedirect('/shop/merci')
    else:
        form = NousContacter()

    return render(request, 'shop/nousContacter.html', {'form': form})

def ft_Merci(request):

    return render(request, 'shop/remerciement.html')

class categories(ListView):
    model=Categories
    paginate_by=25
    
def ft_article(request,pk_categorie):
    q=Articles.objects.all()
    article=[loop for loop in q if loop.categories.id==pk_categorie]

    paginator=Paginator(article, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if len(article)==0:
        return HttpResponse("Ce article n'existe pas")
    else:
        return render(request, 'shop/articles_list.html', {'page_obj':page_obj})

def ft_article_detaille(request,pk_categorie,pk_article):
    
    try:
        article=Articles.objects.get(pk=pk_article)
    except Articles.DoesNotExist:
        raise Http404("Article does not exist")
    return render(request, 'shop/article_detail.html', {'article': article})
    #return HttpResponse("Ici les detaille de l'article")
   
