from django.db import models

# Create your models here.
class Turma(models.Model):
    """ Modelo representando a turma """
    numero = models.AutoField(
        primary_key=True,
        help_text = 'Informe o numero da turma '
    )
    horarioAula = models.IntegerField(
        null=False,
        help_text = 'Informar horario da aula'
    )

    duracaoAula = models.IntegerField(
        null=False,
        help_text = 'Informar duracao aula'
    )
    
    dataInicial = models.DateField(
        null=False,
        help_text = 'Informe a data inicial da aula'
    )
    
    dataFinal = models.DateField(
        null=True,
        help_text = 'Informe Data Final'
    )
    
    codigoTipoAtividade = models.IntegerField(
        null=False,
        help_text = 'Informe Tipo de Atividade'
    )
    
    matriculaMonitor = models.IntegerField(
        null=False,
        help_text= 'Informe matricula monitor'
    )
    
    idInstrutor = models.IntegerField(
        null=False,
        help_text= 'Informe ID do Instrutor'
    )
    
    def __str__(self):
        return f"{self.numero}- {self.horarioAula}- {self.duracaoAula}- {self.dataInicial}- {self.dataFinal}- {self.codigoTipoAtividade}- {self.matriculaMonitor}- {self.idInstrutor}"