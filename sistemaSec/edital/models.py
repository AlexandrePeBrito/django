from django.db import models
from ..programa.models import Programa

class Edital(models.Model):
    id_edital = models.AutoField(primary_key=True)
    quantidade_vagas_edital = models.IntegerField()
    #foreign key
    id_programa_edital = models.ForeignKey(Programa, on_delete=models.PROTECT, related_name="editais")

