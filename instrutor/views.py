from django.http import HttpResponse
from django.shortcuts import render, redirect
from instrutor.forms import InstrutorForm
from instrutor.models import Instrutor

# Create your views here.

def listar(request):
    lista_instrutor = Instrutor.objects.all()
    contexto = {
        'instrutores': lista_instrutor
    }
    return render(request,'instrutor/listarInstrutores.html', context=contexto)

def carregar_cadastro(request):
    return render(request,'instrutor/cadastroInstrutor.html')

def cadastrar(request):
    form = InstrutorForm(request.POST)
    if form.is_valid():
        dados_instrutor = form.cleaned_data
        instrutor = Instrutor (
            id = dados_instrutor['id']
        )
        
        instrutor.save()

    return render(request,'instrutor/cadastroInstrutor.html')

def excluir(request, idInstrutor):
    try:
        instrutor = Instrutor.objects.get(pk=idInstrutor)
        instrutor.delete()
    except Instrutor.DoesNotExist:
        pass
    
    return redirect('instrutor:listar')