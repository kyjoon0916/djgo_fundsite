from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def board(request):
    return render(request, 'board.html')

def writing_list(request):
    writing_list = Writing.objects.all().order_by(‘-created_date’)
    paginator = Paginator(writing_list, 10)
    page = request.POST.get(‘page’)

    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)