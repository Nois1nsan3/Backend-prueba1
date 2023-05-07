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
    doc_externo=open('C:/Users/boriz/OneDrive/Escritorio/Django proyectos/Django_Prueba_1/plantillas/templates/usuario.html')

    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx=Context({
        "title" : "DJANGO SHOP",
        "user" : "Datos de Usuario",
        "nombre" : "Xavier",
        "apellido": "Papito",
        "nacionalidad" : "Hindi",
        "return" : "Volver",
        })

    pagina = plt.render(ctx)

    return HttpResponse(pagina)

