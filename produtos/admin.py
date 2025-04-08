from django.contrib import admin
from .models import Tamanho,Terno, Infantil, Sapato
# Register your models here.

@admin.register(Tamanho)
class TamanhoAdmin(admin.ModelAdmin):
    list_display = ('numero',)
    ordering = ('numero',)
    
    
@admin.register(Terno)
class TernoAdmin(admin.ModelAdmin):
    list_display = ('titulo','descricao','mostrar_tamanhos',)
    list_filter = ('tamanho',)
    search_fields = ('titulo', 'descricao')
    list_display_links = ('titulo',)  # Só o título será clicável para edição
    
    def mostrar_tamanhos(self, obj):
        return " - ".join([str(t) for t in obj.tamanho.all()])
    mostrar_tamanhos.short_description = 'Tamanhos'

@admin.register(Infantil)
class InfantilAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
# admin.site.register(Terno,TernoAdmin)

@admin.register(Sapato)
class SapatoAdmin(admin.ModelAdmin):
    list_display =('titulo', )
    
