from django.shortcuts import render
from .models import Noticia  # Ejemplo de modelo para noticias

def index(request):
    return render(request, 'archivo.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def noticias(request):
   
    return render(request, 'noticias.html')

def inscripciones(request):
    return render(request, 'inscripciones.html')

def contacto(request):
    return render(request, 'contacto.html')

def oferta(request):
    return render(request, 'oferta.html')
