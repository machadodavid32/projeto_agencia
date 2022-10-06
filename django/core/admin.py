from django.contrib import admin

# Register your models here.

from .models import Projetos



class ProjetosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'desc')


admin.site.register(Projetos, ProjetosAdmin)
