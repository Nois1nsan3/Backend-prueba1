from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def celulares(request):
    return render (request, 'celulares.html')


def juegos(request):
    return render (request, 'juegos.html')

