from django.shortcuts import render

# Create your views here.

def projetos(request):
    return render(request, 'meus-projetos.html')


def contato(request):
    return render(request,'contato.html')

