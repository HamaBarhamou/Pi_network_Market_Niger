from django.shortcuts import  HttpResponse
from django.shortcuts import  HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .forms import searchForm


@csrf_exempt
def search(request, search=None):
    if request.method == "POST":
        form = searchForm(request.POST)
        if form.is_valid():
            context = {'form': 'search'}
        else:
            form = searchForm(request.POST)
            context = {'form': ''}   
    else:
        context = {'form': ''}
    template = loader.get_template('search.html')
    return HttpResponse(template.render(context, request))

""" def search(request, search):
    return HttpResponse(f'champ de recherche: {search}') """