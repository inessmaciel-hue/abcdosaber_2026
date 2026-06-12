from django.db import models

# Create your models here.
class Aluno(models.Model):
    """ Modelo representando um Aluno """
    matricula = models.AutoField(
        primary_key=True,
        help_text = 'Código da matricula'
    )

    nome = models.CharField(
        max_length=70,
        null=False,
        help_text= 'Informe o nome'
    )
    
    data_inicial = models.DateField(
        null=False,
        help_text= 'Informe a data'
    )
    
    data_final = models.DateField(
        null=True,
        help_text= 'Informe a data'
    )
    
    def __str__(self):
        return f'{self.matricula} {self.nome}'