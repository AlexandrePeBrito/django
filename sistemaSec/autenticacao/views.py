# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from sistemaSec.estagiario.models import Estagiario
from sistemaSec.supervisor.models import Supervisor


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "cadastro/register.html", {"form": form, "msg": msg, "success": success})


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "cadastro/login.html", {"form": form, "msg": msg})

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

