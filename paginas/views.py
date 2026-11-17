from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria, filme, projeto

def inicio(request):
    contexto = {
        'nome': 'Conrado Vieira',
        'cidade': 'Recife - PE',
        'cursos': ['Programação Back-End.', 'Programação Front-End.', 'Técnico de Sistema de Informação.'],
        'hobbies': ['Séries e Filmes.', 'Músicas.', 'Comer.', 'Dormir.'],
    }
    return render(request, 'inicio.html', contexto)

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def lista_projetos(request):
    contexto = {
        'projetos': projeto.objects.all(),
    }
    return render(request, 'projeto.html', contexto)

def categoria(request):
    contexto = {
        'categorias': Categoria.objects.all(),
    }
    return render(request, 'categoria.html', contexto)

def lista_filmes(request):
    contexto = {
        'filmes': filme.objects.all(),
    }
    return render(request, 'filmes.html', contexto)