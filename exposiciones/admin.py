from django.contrib import admin
from .models import Exposicion

@admin.register(Exposicion)
class ExposicionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'created_at')
    list_filter = ('categoria',)
    search_fields = ('titulo', 'descripcion')
