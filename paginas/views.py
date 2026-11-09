from django.shortcuts import render

from django.http import HttpResponse

def inicio(request):
    dados = {
        'nome': 'Conrado Cavalcanti',
        'idade': 30,
        'altura': 1.69,
        'pets':['Jorel', 'Frederico', 'Hermione', 'Tokio', 'Tunico', 'Zeus', 'Marley', 'Luna', 'Love', 'Nala', 'Pandora', 'Luke', 'Athena']
    }
    return render(request, 'inicio.html', dados)

def sobre(request):
    return HttpResponse("<h1>Minha ONG:</h1>"
                        "<p>Tenho uma ONG que ajuda animais de rua, se quiser ajudar, entre em contato comigo.</p>")

def contato(request):
    return HttpResponse("<h1>Contato </h1>"
                        "<p>Entre em contato comigo pelo e-mail: conradocavalcantii@gmail.com</p>"
                        "<a href='/'>Inicio</a> | "
                        "<a href='/sobre/'>Sobre</a>")