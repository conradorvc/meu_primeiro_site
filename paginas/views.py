from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import filme
from .models import Categoria, projeto
from .forms import CategoriaForm, ProjetoForm

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
    filmes = filme.objects.all()
    contexto = {
        'filmes': filmes
    }
    
    return render(request, 'filmes.html', contexto)

def novo_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_projetos')
    else:
        form = ProjetoForm()
    return render(request, 'novo_projeto.html', {'form': form})

def nova_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria')  # Redireciona para a página de categorias
    else:
        form = CategoriaForm()
    
    return render(request, 'nova_categoria.html', {'form': form})