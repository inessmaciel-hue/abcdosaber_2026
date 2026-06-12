from django.db import models

# Create your models here.

class Titulo(models.Model):
    """ Modelo representando um Titulo """
    codigo = models.AutoField(
        primary_key=True,
        help_text = 'Código do Título'
    )

    descricao = models.CharField(
        max_length=70,
        null=False,
        help_text= 'Informe a descricao do Titulo'
    )
    
    def __str__(self):
        return f'{self.codigo} {self.descricao}'
    

    
