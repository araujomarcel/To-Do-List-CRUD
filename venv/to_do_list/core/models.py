from django.db import models
from datetime import datetime

# Create your models here.

class AtividadeModel(models.Model):
    nome = models.CharField(max_length=80)
    tipo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)
    data = models.DateField()
    modificado_em = models.DateTimeField(verbose_name='modificado em', auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural='Atividades'
        verbose_name='Atividade'
        ordering=('data', 'modificado_em')
            
