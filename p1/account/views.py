from datetime import datetime
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from account.models import User, UserAuth
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
# SMTP 관련 인증
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from account.tokens import account_activation_token


def index(request):
    print('invoke account.views.index')
    print(request)
    print('request.user',request.user)
    user = request.session.get('user')
    return render(request, 'index.html',)

"""
--> login
* base_user.py --> set_unusable_password()
1. Compare password with db and return results
    1-0. user.is_authenticated --> return always True --> 
    whether ``user`` is None or not --> Only need to set ``user`` and return that named user
    1-1. set_password --> 
2. If equal, set session and persist authentication

--> logout
1. remove session
"""
def login_view(request):
    response_data = {}
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = UserAuth().authenticate(email=email, password=password)

        if user is not None:
            print('user is', user)
            response_data['result'] = 'ok'
            # Todo --> set session with django built-in function
            # request.session['user'] = user.email
            login(request, user)
            user.last_login = datetime.today().strftime('%Y-%m-%d') +' '+ datetime.today().strftime('%H:%M:%S')
            user.save()
            return JsonResponse(response_data)
        else:
            print('user is None')
            response_data['result'] = 'error'
            response_data['msg'] = '아이디와 비밀번호를 확인해주세요.'
            return JsonResponse(response_data)
    # return redirect(request.META.get('HTTP_REFERER', 'index.html'))

def logout_view(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER', 'index.html'))


def get_user_info(request):
    try:
        user = User.objects.get(email=request)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    return user


def check_email(request):
    if request.method == 'POST' :
    
        response_data = {}
        user = get_user_info(request.POST['email'])

        # if user is not None and user.is_active == 1:
        #     response_data['result'] = 'error'
        #     response_data['msg'] = '이미 가입된 계정입니다.'
        #     return JsonResponse(response_data)
        # elif user is not None and user.is_active == 0:
        #     print('!!')
        if user is not None:
            response_data['result'] = 'error'
            response_data['msg'] = '이미 가입된 계정입니다.'
            return JsonResponse(response_data)
        else:
            response_data['result'] = 'ok'
            return register_confirmEmail(request, response_data)
        
    else :
        return redirect(request, 'account/register_email.html')


def register_confirmEmail(request, response_data):
    user = User.objects.create_user(email=request.POST['email'])

    message = render_to_string('account/activation_email.html', {
        'domain': request.get_host(),
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })
    mail_title = "[스마트시티 리빙랩] 계정 활성화 확인 이메일"
    mail_to = request.POST['email']
    email = EmailMessage(mail_title, message, to=[mail_to])
    email.send()

    return JsonResponse(response_data)


def check_certification(request):
    user = get_user_info(request.POST['email'])
    if user is None:
        return HttpResponse('이메일 인증코드를 받으신 뒤 다시 시도해 주십시오.')

    return HttpResponse(user.is_active)


# 계정 활성화 함수(토큰을 통해 인증)
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect(index)
    else:
        # return render(request, '.html', {'error' : '계정 활성화 오류'})
        return redirect(index)


def register_result(request):
    user = User.objects.update_user(request)

    return redirect(index)