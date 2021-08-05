from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.index),
    path('', views.about),
    url(r'^$', views.Writingview.as_view(), name='post'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)