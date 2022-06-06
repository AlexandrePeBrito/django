from django.db import models

class Supervisor(models.Model):
    id_supervisor = models.AutoField(primary_key=True)
    nome_supervisor = models.CharField(max_length=200)
    telefone_supervisor = models.CharField(max_length=12)
    email_supervisor = models.CharField(max_length=200)
    def __str__(self):
        return self.nome_supervisor