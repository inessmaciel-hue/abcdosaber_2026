from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def cadastrar(request):
    return render(request,'contato/contato.html')


