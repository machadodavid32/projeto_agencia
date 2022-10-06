from inspect import ClassFoundException
from unittest.util import _MAX_LENGTH
from django.db import models

class Projetos(models.Model):
    nome = models.CharField('nome', max_length=100)
    desc = models.CharField('descricao', max_length=500)

    def __str__(self) -> str:   # Esta função serve para que o nome do projeto apareça na tela de projetos do adm do site
        return self.nome
    




