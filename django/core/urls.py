from django.urls import path

from core.views import index, projetos, contato, sobremim

urlpatterns = [
     path('projetos', projetos),
     path('contato', contato),
     path('', index),
     path('sobremim', sobremim)
     
]