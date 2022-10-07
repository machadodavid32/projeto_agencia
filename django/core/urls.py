from django.urls import path

from core.views import index, projetos, contato, sobremim

urlpatterns = [
     path('', index),
     path('contato.html', contato, name='contato'),
     path('meus-projetos.html', projetos, name='projetos'),
     path('sobremim.html', sobremim, name='sobremim'),
     
]

