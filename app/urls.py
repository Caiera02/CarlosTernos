from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from produtos.views import terno_view, home_view, sapato_view,camisa_view,TernoDetailview,TernoDeleteView
from acessorios.views import acessorios_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view, name= 'home' ),
    path('terno/',terno_view, name='terno_list'),
    path('terno/<int:pk>/',TernoDetailview.as_view(), name='terno_detail'),
    path('terno/<int:pk>/delete/', TernoDeleteView.as_view(), name='terno_delete'),
    path('acessorios/',acessorios_view, name='Acessorios_list'),
    path('sapato/',sapato_view, name='sapato_list'),
    path('camisa/',camisa_view, name='camisa_list'),
]+ static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)