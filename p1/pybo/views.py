from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, JsonResponse
from .models import Writing, FundingLog
from account.models import User
from datetime import datetime

def index(request):
    writing_list = Writing.objects.order_by('pub_date') 
    page = request.GET.get('page', 1)
    paginator = Paginator(writing_list, 3)
    writings = paginator.get_page(page)
    return render(request, 'index.html', {'writings': writings,})


def about(request, id):
    writing = Writing.objects.get(pk=id)
    tags = writing.tag.split('/')
    return render(request, 'about.html', {'writing': writing, 'tags': tags})


def fundingupdate(request):
    response_data = {}

    if request.method == 'POST':
        response_data['result'] = 'ok'
        user_id = int(request.POST['user_id'])
        writing_id = int(request.POST['writing_id'])
        funding_amount = int(request.POST['funding_amount'])
        
        # update user.balance
        user = User.objects.filter(id=user_id)
        print('updated balance=',(user.first().balance-funding_amount))
        user.update(balance=(user.first().balance-funding_amount))

        # update writing.accumulated_amount
        writing = Writing.objects.filter(id=writing_id)
        print('updated accumulated_amount=', (writing.first().accumulated_amount + funding_amount))
        writing.update(accumulated_amount=(writing.first().accumulated_amount + funding_amount))

        # save the funding log
        funding_log = FundingLog(user_id=User.objects.get(id=user_id), writing_id=Writing.objects.get(id=writing_id), funding_amount=funding_amount, funding_date=datetime.now())
        funding_log.save()
        return JsonResponse(response_data)
    else:
        response_data['result'] = 'error'
        return JsonResponse(response_data)

    
    return None

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