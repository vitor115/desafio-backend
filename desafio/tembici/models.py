from django.db import models

class Trip(models.Model):
    data_inicio = models.DateField()
    data_fim = models.DateField()
    classificacao = models.SmallIntegerField()
    nota = models.SmallIntegerField()