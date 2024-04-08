from django.shortcuts import render
from django.http import HttpResponse

dados = {
    1: {
        "nome": "Nebulosa de Carina",
        "legenda": "webbtelecope.org/NASA/James Webb"    
    }, 
    2: {
        "nome": "Galáxia NGC 1079",
        "legenda": "Qualquer coisa"
    },

}

def index(request):
    return render(request, "galeria/index.html", {"cards": dados})

def imagem(request):
    return render(request, "galeria/imagem.html")