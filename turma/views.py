from django.http import HttpResponse
from django.shortcuts import render, redirect
from turma.models import Turma

# Create your views here.

def cadastrar(request):
    return render(request,'turma/cadastroTurma.html')

def listar(request):
    lista_turma = Turma.objects.all()
    contexto = {
        'lista_turma': lista_turma
    }
    return render(request,'turma/listarTurmas.html', context=contexto)

def registrar(request):
    return render(request,'turma/registroAusencia.html')

def excluir(request,numeroTurma):
    try:
        turma = Turma.objects.get(pk=numeroTurma)
        turma.delete()
    except Turma.DoesNotExist:
        pass
    
    return redirect('turma:listar')