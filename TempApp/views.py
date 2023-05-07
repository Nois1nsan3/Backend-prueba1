from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context


        

# Create your views here.

def index(request):
    return render (request, "templates/index.html")


def celulares(request):
    return render (request, 'templates/celulares.html')


def juegos(request):
    return render (request, 'templates/juegos.html')

def usuario(request):
    doc_externo = open('plantillas/templates/usuario.html')


    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx=Context({
        'nombre' : 'Nois',
        'sub' : 'Web Design & Development',
        'telefono' : '+569 93053395',
        'email' : 'boriznicolaz@gmail.com',
        'web' : 'www.Nois1ns4n3.com',
        'return' : "Volver",
        })

    pagina = plt.render(ctx)

    return HttpResponse(pagina)

