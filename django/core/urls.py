from django.urls import path

from core.views import index, projetos, contato, sobremim

urlpatterns = [
     path('', index),
     path('contato', contato),
     path('projetos', projetos),
     path('sobremim', sobremim),
     
]

