from django.contrib import admin
from .models import Terno
# Register your models here.

@admin.register(Terno)
class TernoAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    # search_fields = ('descricao',)

# admin.site.register(Terno,TernoAdmin)