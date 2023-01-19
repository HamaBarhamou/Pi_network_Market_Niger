from django.shortcuts import  HttpResponse
from django.shortcuts import  HttpResponse
from django.template import loader

def home(request):
    context = {'form': 'form'}
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))