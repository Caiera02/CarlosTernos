from django.contrib import admin
from .models import Terno, Infantil, Tamanho
# Register your models here.


@admin.register(Tamanho)
class TamanhoAdmin(admin.ModelAdmin):
    list_display = ('numero',)
    
@admin.register(Terno)
class TernoAdmin(admin.ModelAdmin):
    list_display = ('titulo','descricao',)
    # search_fields = ('descricao',)

@admin.register(Infantil)
class InfantilAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
# admin.site.register(Terno,TernoAdmin)