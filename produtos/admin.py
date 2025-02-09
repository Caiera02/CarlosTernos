from django.contrib import admin
from .models import Terno, Infantil
# Register your models here.

@admin.register(Terno)
class TernoAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    # search_fields = ('descricao',)

@admin.register(Infantil)
class InfantilAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
# admin.site.register(Terno,TernoAdmin)