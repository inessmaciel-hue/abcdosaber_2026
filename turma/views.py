from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def cadastrar(request):
    return render(request,'turma/cadastroTurma.html')

def listar(request):
    return render(request,'turma/listarTurmas.html')

def registrar(request):
    return render(request,'turma/registroAusencia.html')