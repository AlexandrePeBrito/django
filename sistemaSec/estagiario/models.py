"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from ..supervisor.models import Supervisor

class Estagiario(models.Model):
    cpf_estagiario = models.CharField(primary_key=True, max_length=11)
    nome_estagiario = models.CharField(max_length=200)
    rg_estagiario = models.CharField(max_length=11)
    turno_estagiario = models.CharField(max_length=25)
    email_estagiario = models.CharField(max_length=200)
    semestre_estagiario = models.IntegerField()
    nis_pis_estagiario = models.CharField(max_length=12)
    telefone_estagiario = models.CharField(max_length=12)
    nome_responsavel_estagiario = models.CharField(max_length=200)
    data_nascimento_estagiario = models.CharField(max_length=10)
    genero_estagiario = models.CharField(max_length=12)
    raca_estagiario = models.CharField(max_length=10)
    bairro_estagiario = models.CharField(max_length=200)
    numero_estagiario = models.CharField(max_length=15)
    complemento_estagiario = models.CharField(max_length=200)
    matricula_estagiario = models.CharField(max_length=20)
    situacao_estagiario = models.CharField(max_length=200)
    #FOREIGN KEY
    supervisor_estagiario = models.ForeignKey(Supervisor, on_delete=models.CASCADE, related_name="estagiarios", null = True)
    
    def __str__(self):
        return self.nome_estagiario

