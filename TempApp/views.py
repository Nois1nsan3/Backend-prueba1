from django.shortcuts import render
from django.http import HttpResponse

        

# Create your views here.

def index(request):
    return render (request, "templates/index.html")


def celulares(request):
    return render (request, 'templates/celulares.html')


def juegos(request):
    return render (request, 'templates/juegos.html')

def usuario(request):
    return HttpResponse ("Bienvenido a la pagina de usuario")

