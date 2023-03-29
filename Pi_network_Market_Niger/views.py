from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from shop.models import Article
from django.db.models import Count
from django.db.models import F


def search(request):
    query = request.GET.get('q')
    if query:
        articles = Article.objects.filter(name__icontains=query)
    else:
        articles = Article.objects.none()  # retourner une queryset vide si q est None

    # Ajouter la pagination
    paginator = Paginator(articles, 10)
    page = request.GET.get('page')
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)

    # Récupérer les 5 articles les plus consultés
    top_articles = Article.objects.order_by('-views_count')[:5]

    context = {'articles': results, 'query': query, 'top_articles': top_articles}
    return render(request, 'search_results.html', context)


