from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from produtos.views import terno_view, home_view
from acessorios.views import acessorios_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',home_view, name= 'home' ),
    path('terno/',terno_view, name='terno_list'),
    path('acessorios/',acessorios_view, name='Acessorios_list'),
]+ static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)