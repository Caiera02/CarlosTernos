from django.contrib import admin
from acessorios.models import Acessorios

# Register your models here.

@admin.register(Acessorios)
class AcessoriosAdmin(admin.ModelAdmin):
    list_display = ('nome','cor','img')
    
