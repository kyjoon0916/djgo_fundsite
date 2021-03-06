from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from common.forms import UserForm
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    return render(request, 'index.html')

@csrf_protect
def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            # user = authenticate(email=email, password=raw_password)
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            #login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

def bad_request_page(request, exception):
    response = render_to_response('error/error_400_page.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 400
    return response

def permission_denied(request, exception):
    response = render_to_response('error/error_403_page.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 403
    return response

def page_not_found(request, exception):
    response = render_to_response('error/error_404_page.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

def server_error(request):
    response = render_to_response('error/error_500_page.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
