from django.urls import path

from .views import projetos, contato

urlpatterns = [
     path('projetos', projetos),
     path('contato', contato),

]