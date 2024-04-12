from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "home.html", context={"name": "Paulo"})

def contato(request):
    return HttpResponse("CONTATO")

def sobre(request):
    return HttpResponse("SOBRE")