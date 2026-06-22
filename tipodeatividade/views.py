from django.http import HttpResponse
from django.shortcuts import render, redirect
from tipodeatividade.form import TipoAtividadeForm
from tipodeatividade.models import Tipodeatividade

# Create your views here.

def listar(request):
    lista_tipodeatividade = Tipodeatividade.objects.all()
    contexto = {
        'lista_tipodeatividade': lista_tipodeatividade
    }
    return render(request, 'tipodeatividade/listarTiposAtividade.html', context=contexto)

def carregar_cadastro(request):
    return render(request, 'tipodeatividade/cadastroTiposAtividade.html')

def cadastrar(request):
    form = TipoAtividadeForm(request.POST)
    if form.is_valid():
        dados_tipodeatividade = form.cleaned_data
        tipodeatividade = Tipodeatividade(
            descricao = dados_tipodeatividade['descricao']
        )
        
        tipodeatividade.save()
        
    return render(request, 'tipodeatividade/cadastroTiposAtividade.html')


def excluir(request, codigoTipodeatividade):
    try:
        tipodeatividade = Tipodeatividade.objects.get(pk=codigoTipodeatividade)
        tipodeatividade.delete()
    except Tipodeatividade.DoesNotExist:
        pass
    
    return redirect('tipodeatividade:listar')
        
