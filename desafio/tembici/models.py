from django.db import models
import datetime

class Trip(models.Model):
    opcoes = (
        (1, 'Trabalho'),
        (2, 'Atividade física'),
        (3, 'Lazer'),
        (4, 'Deslocamento'),
    )
    data_inicio = models.DateTimeField(default = datetime.datetime.now())
    data_fim = models.DateTimeField(default = datetime.datetime.now())
    classificacao = models.SmallIntegerField(choices=opcoes)
    nota = models.SmallIntegerField(default=1)