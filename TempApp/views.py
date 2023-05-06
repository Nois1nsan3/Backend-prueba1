from django.shortcuts import render
from django.http import HttpResponse

        

# Create your views here.

def index(request):
    return render (request, "Hello, world. You're at the polls index.")


def celulares(request):
    return render (request, 'templates/celulares.html')


def juegos(request):
    return render (request, 'templates/juegos.html')

def usuario(request):
    return HttpResponse ("Hola, usuario")

