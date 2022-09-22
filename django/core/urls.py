from django.urls import path

from .views import index, projetos, contato

urlpatterns = [
     path('projetos', projetos),
     path('contato', contato),
     path('', index),
     

]