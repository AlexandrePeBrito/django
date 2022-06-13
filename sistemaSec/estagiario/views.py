# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from sistemaSec.estagiario.models import Estagiario
from sistemaSec.supervisor.models import Supervisor

@login_required(login_url="/login/")
def criar_estagiario_partiu_estagio(request):
    if request.method == "POST":
        nome_estagiario = request.POST['nome_estagiario']
        cpf = request.POST['cpf']
        rg = request.POST['rg']
        turno = request.POST['turno']
        email = request.POST['email']
        semestre = request.POST['semestre']
        nis = request.POST['nis']
        telefone = request.POST['telefone']
        responsavel = request.POST['responsavel']
        nascimento = request.POST['nascimento']
        genero = request.POST['genero']
        raca = request.POST['raca']
        bairro = request.POST['bairro']
        numero = request.POST['numero']
        complemento = request.POST['complemento']
        Matricula = request.POST['Matricula']
        situaçao = request.POST['situaçao']
        supervisor = request.POST['supervisor']

        supervisorObj = Supervisor.objects.get(id_supervisor=supervisor)
        estagiario = Estagiario.objects.create(cpf_estagiario = cpf,
            nome_estagiario = nome_estagiario, rg_estagiario = rg,
            turno_estagiario = turno, email_estagiario = email,
            semestre_estagiario = semestre, nis_pis_estagiario = nis,
            telefone_estagiario = telefone, nome_responsavel_estagiario = responsavel,
            data_nascimento_estagiario = nascimento,
            genero_estagiario = genero, raca_estagiario = raca,
            bairro_estagiario = bairro, numero_estagiario = numero,
            complemento_estagiario = complemento, matricula_estagiario = Matricula,
            situacao_estagiario = situaçao, supervisor_estagiario = supervisorObj)
        
        estagiario.save()
        return redirect("/")
    else:
        return redirect("sistemaSec/templates/home/PAES_criar_estagiario.html")

@login_required(login_url="/login/")
def consultar_estagiario_partiu_estagio(request):
    
    estagiarios = Estagiario.objects.all()
    
        
    if 'buscar_estagiario_partiu_estagio' in request.GET:
        nome_consulta=request.GET['buscar_estagiario_partiu_estagio']
        cpf_consulta=request.GET['buscar_estagiario_partiu_estagio']

        if consultar_estagiario_partiu_estagio:
            lista = estagiarios.filter(Q(nome_estagiario__icontains=nome_consulta)|Q(cpf_estagiario__icontains=cpf_consulta))
            

    dados = {
        "estagiarios": lista
    }

    return render(request,"home/PAES_buscar_estagiario.html",dados)
    
@login_required(login_url="/login/")    
def editar_estagiario_partiu_estagio(request,cpf_estagiario):
    estagiario = get_object_or_404(Estagiario, pk=cpf_estagiario)
    editar_estagiario = { 'estagiario':estagiario }
    return render(request, 'home/PAES_editar_estagiario.html', editar_estagiario)

@login_required(login_url="/login/")
def atualizar_estagiario_partiu_estagio(request):
    if request.method == 'POST':
        cpf = request.POST['cpf']
        est = Estagiario.objects.get(pk=cpf)
        est.nome_estagiario = request.POST['nome_estagiario']
        est.cpf_estagiario = cpf
        est.rg_estagiario = request.POST['rg']
        est.turno_estagiario = request.POST['turno']
        est.email_estagiario = request.POST['email']
        est.semestre_estagiario = request.POST['semestre']
        est.nis_pis_estagiario = request.POST['nis']
        est.telefone_estagiario = request.POST['telefone']
        est.nome_responsavel_estagiario = request.POST['responsavel']
        est.data_nascimento_estagiario = request.POST['nascimento']
        est.genero_estagiario = request.POST['genero']
        est.raca_estagiario = request.POST['raca']
        est.bairro_estagiario = request.POST['bairro']
        est.numero_estagiario = request.POST['numero']
        est.complemento_estagiario = request.POST['complemento']
        est.matricula_estagiario = request.POST['Matricula']
        est.situacao_estagiario = request.POST['situaçao']
        supervisor = request.POST['supervisor']
        supervisorObj = Supervisor.objects.get(id_supervisor=supervisor)
        est.supervisor_estagiario = supervisorObj
        est.save()

        estagiarios = Estagiario.objects.all()
        dados = {
            "estagiarios":estagiarios
        }
        return render(request,"home/PAES_dashboard.html",dados)
    else:
        return redirect("home/PAES_criar_estagiario.html")

