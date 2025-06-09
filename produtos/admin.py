from django.contrib import admin
from produtos.models import Tamanho,Terno, Sapato, Camisa

@admin.register(Tamanho)
class TamanhoAdmin(admin.ModelAdmin):
    list_display = ('numero',)
    ordering = ('numero',)
    
    
@admin.register(Terno)
class TernoAdmin(admin.ModelAdmin):
    list_display = ('titulo','descricao','mostrar_tamanhos',)
    list_filter = ('tamanho',)
    search_fields = ('titulo', 'descricao')
    ordering = ('titulo',)
    
    def mostrar_tamanhos(self, obj):
        return " - ".join([str(t) for t in obj.tamanho.all()])
    mostrar_tamanhos.short_description = 'Tamanhos'

# @admin.register(Infantil)
# class InfantilAdmin(admin.ModelAdmin):
#     list_display = ('titulo',)
#     ordering = ('titulo',)

@admin.register(Sapato)
class SapatoAdmin(admin.ModelAdmin):
    list_display =('titulo','tamanho','descricao',)
    ordering = ('titulo',)
    
@admin.register(Camisa)
class CamisaAdmin(admin.ModelAdmin):
    list_display =('titulo','tamanho' )   
    ordering = ('titulo',)
