from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from sistemaSec.sede.models import Sede
from sistemaSec.municipio.models import Municipio
from sistemaSec.nte.models import NTE


@login_required(login_url="/login/")
def criar_sede(request):
    if request.method == "POST":
        nome_sede = request.POST['nome_sede']
        codigo_inep_sede = request.POST['codigo_inep_sede']
        telefone_sede = request.POST['telefone_sede']
        nome_responsavel_sede = request.POST['nome_responsavel_sede']
        bairro_sede = request.POST['bairro_sede']
        email_sede = request.POST['email_sede']
        id_nte_sede = request.POST['id_nte_sede']
        id_municipio_sede = request.POST['id_municipio_sede']
        
        nte = NTE.objects.get(id_NTE=id_nte_sede)
        municipio = Municipio.objects.get(id_municipio=id_municipio_sede)

        sede = Sede.objects.create(nome_sede = nome_sede,
        codigo_inep_sede = codigo_inep_sede, telefone_sede = telefone_sede,
        nome_responsavel_sede = nome_responsavel_sede, bairro_sede = bairro_sede,
        email_sede = email_sede, id_nte_sede = nte,
        id_municipio_sede = municipio)
        
        sede.save()
        return redirect("/")
    else:
        return redirect("sistemaSec/templates/home/SEDE_criar_sede.html")

@login_required(login_url="/login/")
def consultar_sede(request):
    lista_por_sede=None
    sede = Sede.objects.all()
    
    if 'buscar_sede' in request.GET:
        sede_consulta=request.GET['buscar_sede']
        bairro_consulta=request.GET['buscar_bairro']
        municipio_consulta=request.GET['buscar_municipio']
        if consultar_sede:
            lista_por_sede = sede.filter(Q(nome_sede__icontains=sede_consulta))
            lista_por_bairro = lista_por_sede.filter(Q(bairro_sede__icontains = bairro_consulta))
            lista_por_municipio = lista_por_bairro.filter(Q(id_municipio_sede__nome_municipio__icontains = municipio_consulta))
    
    dados = {"sedes": lista_por_municipio}
    return render(request,"home/SEDE_buscar_sede.html",dados)
    
@login_required(login_url="/login/")    
def editar_sede(request,id_sede):
    sede = get_object_or_404(Sede, pk=id_sede)
    edt_sede = { 'sede':sede }
    return render(request, 'home/SEDE_editar_sede.html', edt_sede)

@login_required(login_url="/login/")
def atualizar_sede(request):
    if request.method == 'POST':
        cod_sede = request.POST['id_sede']
        sed = Sede.objects.get(pk=cod_sede)
        sed.id_sede = cod_sede
        sed.nome_sede = request.POST['nome_sede']
        sed.codigo_inep_sede = request.POST['codigo_inep_sede']
        sed.telefone_sede = request.POST['telefone_sede']
        sed.nome_responsavel_sede = request.POST['nome_responsavel_sede']
        sed.bairro_sede = request.POST['bairro_sede']
        sed.email_sede = request.POST['email_sede']

        id_nte_sede = request.POST['id_nte_sede']
        nte = NTE.objects.get(id_NTE=id_nte_sede)
        id_municipio_sede = request.POST['id_municipio_sede']
        municipio = Municipio.objects.get(id_municipio = id_municipio_sede)

        sed.id_nte_sede = nte
        sed.id_municipio_sede = municipio
        sed.save()

        sede = Sede.objects.all()
        dados ={'sedes': sede}
        return render(request, 'home/SEDE_dashboard.html',dados)
    else:
        return redirect("home/SEDE_criar_sede.html")
