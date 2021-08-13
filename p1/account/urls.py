from django.urls import path

from . import views

urlpatterns = [
    path('../', views.index, name='index'),
    path('check_email', views.check_email, name='check_email'),
    path('check_certification', views.check_certification, name='check_certification'),
    # path('register_email', views.register_email, name='register_email'),
    # path('register_info', views.register_info, name='register_info'),
    # path('register_info/<str:email>', views.register_info, name='register_chk'),
    # path('register_confirmEmail', views.register_confirmEmail, name = 'register_confirmEmail'),
    path('register_result', views.register_result, name = 'register_result'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name="activate"),
]