from django import forms

class InstrutorForm(forms.Form):
    rg = forms.CharField(
        required=False,
        max_length=15,
        help_text = 'Informe RG do Instrutor'
    )
    
    nome = forms.CharField(
        required=True,
        max_length=70,
        help_text='Informe nome do Instrutor'
    )
    
    data_nascimento = forms.DateField(
        required=True,
        help_text='Informe Data de nascimento do instrutor'
    )
    
    telefone = forms.CharField(
        required=False,
        max_length=9,
        help_text='Informe numero de telefone'
    )
    
    ddd = forms.CharField(
        required=False,
        max_length=3,
        help_text='Informe o numero do DDD'
    )
    
    codigo_titulo = forms.IntegerField(
        required=False,
        help_text='Informe código título do instrutor'
    )
    
    