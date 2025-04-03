from django.contrib import admin
from .models import Terno, Infantil, Tamnho
# Register your models here.

@admin.register(Tamnho)
class TamanhoAdmin(admin.ModelAdmin):
    list_display =( 'size',)

@admin.register(Terno)
class TernoAdmin(admin.ModelAdmin):
    list_display = ('titulo','descricao',)
    # search_fields = ('descricao',)

@admin.register(Infantil)
class InfantilAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
# admin.site.register(Terno,TernoAdmin)