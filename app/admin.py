from django.contrib import admin

from app.models import Musica


# Register your models here.
@admin.register(Musica)
class MusicaAdmin(admin.ModelAdmin):
    list_filter = ('banda', 'genero', 'ano')
    list_display = ('nome', 'banda', 'genero', 'ano')
    search_fields = ('nome', 'banda', 'genero', 'ano')
