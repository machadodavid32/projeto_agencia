from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'teste': 'Isso é só um teste'
    }
    return render(request, 'index.html', context)


def projetos(request):
    return render(request, 'meus-projetos.html')


def contato(request):
    context = {'teste': 'Isso é mais um teste' }
    return render(request,'contato.html')


def sobremim(request):
    return render(request, 'sobremim.html', context)


