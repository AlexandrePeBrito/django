from django.db import models

class Programa(models.Model):
    id_programa = models.AutoField(primary_key=True)
    nome_programa = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_programa