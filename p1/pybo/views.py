from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.db import Writing
# Create your views here.
from django.http import HttpResponse
from django.db import models
from .models import Writing
from django.views.generic.list import ListView

def index(request):
    return render(request, 'index.html')
    
def about(request):
    return render(request, 'about.html')

def board(request):
    return render(request, 'board.html')


def home(request):
    numbers_list = range(1, 1000)
    page = request.GET.get('page', 1)
    paginator = Paginator(numbers_list, 20)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'pybo/writings.html', {'numbers': numbers})

class Writingview(ListView):
    model = Writing
    paginate_by = 5
    context_object_name = 'writings'
    template_name = 'writings.html'
    ordering = ['pub_date']