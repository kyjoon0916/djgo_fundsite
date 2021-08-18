from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.db import Writing
# Create your views here.
from django.http import HttpResponse
from .models import Writing
# from p1.account.models import User
from account.models import User


def index(request):
    print('invoke pybo.index')
    # User.objects.delete_user(email='jyh@smartinside.ai')
    print(request.session)
    print('request.user',request.user)
    user = request.session.get('user')
    writing_list = Writing.objects.order_by('pub_date') 
    page = request.GET.get('page', 1)
    paginator = Paginator(writing_list, 3)
    writings = paginator.get_page(page)
    return render(request, 'index.html', {'writings': writings,})


def about(request, id):
    writing = Writing.objects.get(pk=id)
    return render(request, 'about.html', {'writing': writing})


# def home(request):
#     numbers_list = range(1, 1000)
#     page = request.GET.get('page', 1)
#     paginator = Paginator(numbers_list, 20)
#     try:
#         numbers = paginator.page(page)
#     except PageNotAnInteger:
#         numbers = paginator.page(1)
#     except EmptyPage:
#         numbers = paginator.page(paginator.num_pages)
#     return render(request, 'pybo/writings.html', {'numbers': numbers})


# def post_like(request):
#     post = get_object_or_404(Post, id=request.POST.get('post_id'))
#     is_liked = post.likes.filter(id = request.user.id).exists()
#     print("현재 사용자 : ", request.user)
#     print("게시물 정보 : ", post)
#     print("post.likes.filter(Before) :", post.likes.filter(id = request.user.id))
#     print("is_liked :",is_liked)

#     if is_liked :
#         print("좋아요 취소했습니다.")
#         post.likes.remove(request.user)
#         print("post.likes.filter(After) : ", post.likes.filter(id = request.user.id))
#     else:
#         print("좋아요를 눌렀습니다.")
#         post.likes.add(request.user)
#         print("post.likes.filter(After) : ", post.likes.filter(id = request.user.id))

#     return HttpResponseRedirect(reverse('post_detail', kwargs = {'writing':post.id}))