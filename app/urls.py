from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from produtos.views import terno_view, home_view, sapato_view
from acessorios.views import acessorios_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',home_view, name= 'home' ),
    path('terno/',terno_view, name='terno_list'),
    path('acessorios/',acessorios_view, name='Acessorios_list'),
    path('sapato/',sapato_view, name='sapato_list'),
    path('camisa/',sapato_view, name='camisa_list'),
]+ static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)

# Adiciona o suporte a arquivos estáticos (CSS, JS etc.)
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)