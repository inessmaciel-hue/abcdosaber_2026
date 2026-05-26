from django.http import HttpResponse
from django.shortcuts import render

def matricula(request):
    return HttpResponse('<p>Minha View Aluno</p>')

# Create your views here.
