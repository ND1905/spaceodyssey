from django.shortcuts import render
from django.http import HttpResponse
from .models import news,blog
from math import ceil

# Create your views here.

def index(request):
    new = news.objects.all()
    blogs=blog.objects.all()
    # print(new)
    n1=len(blogs)
    n = len(new)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    nSlides=n
    params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'news': new, 'length':n1, 'blog':blogs}

    return render(request, 'space.html', params)