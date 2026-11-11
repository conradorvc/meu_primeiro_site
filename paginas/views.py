from django.shortcuts import render

from django.http import HttpResponse

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

def projeto(request):
    projetos = {
        'projeto': ['Meu Portfólio.', 'Minha ONG.', 'Meu Blog.'],
    }
    return render(request, 'projeto.html', projetos)