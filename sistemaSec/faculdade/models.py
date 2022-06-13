from django.db import models

class Faculdade(models.Model):
    id_faculdade = models.AutoField(primary_key=True)
    nome_faculdade = models.CharField(max_length=200)
    cnpj_faculdade = models.CharField(max_length=14)
    nome_direitor_faculdade = models.CharField(max_length=100)
    telefone_faculdade = models.CharField(max_length=13)
    campus_faculdade = models.CharField(max_length=50)