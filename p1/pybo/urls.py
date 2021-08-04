from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index),
    path('', views.about),
    url(r'^$', views.Writingview.as_view(), name='post'),
    url(r'^fake/$', views.generate_fake_data, name='generate_fake_data'),
]