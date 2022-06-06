"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Estagiario

class ListandoEstagiario(admin.ModelAdmin):
    list_display = ('cpf_estagiario', 'nome_estagiario', 'situacao_estagiario','supervisor_estagiario')
    list_display_links = ('cpf_estagiario', 'nome_estagiario')
    search_fields = ('nome_estagiario','situacao_estagiario','turno_estagiario','semestre_estagiario','bairro_estagiario','supervisor_estagiario')
    list_per_page: 20
    
admin.site.register(Estagiario,ListandoEstagiario)

