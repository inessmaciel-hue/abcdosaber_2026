from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def show_view(request):
    return HttpResponse('<p>Minha View do App Titulos</p>')

def show_template(request):
    return HttpResponse('<p>Esse e o template do site</>')