from multiprocessing import context
from django.shortcuts import render

from .models import Projetos


# Create your views here.

def index(request):
    return render(request, 'index.html')


def projetos(request):
    proj = Projetos.objects.all()
    context = {'proj': proj}

    return render(request, 'meus-projetos.html', context)


def contato(request):
    return render(request,'contato.html')


def sobremim(request):
    return render(request, 'sobremim.html')


