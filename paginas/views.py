from django.shortcuts import render

from django.http import HttpResponse

def inicio(request):
    contexto = {
        'nome': 'Conrado Vieira',
        'cidade': 'Recife',
        'cursos': ['Programação Back-End', 'Programação Front-End'],
        'hobbies':['Jogos', 'Filmes', 'Viagem', 'Comer', 'Dormir']
    }
    return render(request, 'inicio.html', contexto)

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')