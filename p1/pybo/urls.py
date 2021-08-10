from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('f-items/<int:id>', views.item_detail, name='item_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)