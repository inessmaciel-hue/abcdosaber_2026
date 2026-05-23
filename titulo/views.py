from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def show_views(request):
    return HttpResponse('<p>Minha View do App Titulos</p>')

def show_template(request):
    return HttpResponse('<p>Esse e o template do site</>')

def listar_exemplo(request):
    pagina = 'ola'
    return HttpResponse(pagina)

def abc(request):
    pagina = 'ABC!'
    return HttpResponse(pagina)

def index(request):
    return render(request, 'index.html')

def teste(request):
    return render(request, 'teste.html')