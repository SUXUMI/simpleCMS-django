from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Page

def view(request, slug):
    try:
        page = Page.objects.get(slug=slug)
        
        return render(request, 'pages/page.html', {'page': page})
    except Page.DoesNotExist:
        raise Http404()