from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from sistemaSec.faculdade.models import Faculdade

@login_required(login_url="/login/")
def criar_faculdade(request):
    if request.method == "POST":
        nome_faculdade = request.POST['nome_faculdade']
        cnpj_faculdade = request.POST['cnpj_faculdade']
        direitor_faculdade = request.POST['direitor_faculdade']
        campus = request.POST['campus']
        telefone = request.POST['telefone']
        
        faculdade = Faculdade.objects.create(nome_faculdade = nome_faculdade,
            cnpj_faculdade = cnpj_faculdade, nome_direitor_faculdade = direitor_faculdade,
            telefone_faculdade = telefone, campus_faculdade = campus)
        
        faculdade.save()
        return redirect("/")
    else:
        return redirect("sistemaSec/templates/home/FACU_criar_faculdade.html")

@login_required(login_url="/login/")
def consultar_faculdade(request):
    lista_por_nome=None
    faculdade = Faculdade.objects.all()
    
    if 'buscar_faculdade' in request.GET:
        nome_consulta=request.GET['buscar_faculdade']

        if consultar_faculdade:
            lista_por_nome = faculdade.filter(Q(nome_faculdade__icontains=nome_consulta))
            
    dados = {"faculdades": lista_por_nome}
    return render(request,"home/FACU_buscar_faculdade.html",dados)
    
@login_required(login_url="/login/")    
def editar_faculdade(request,id_faculdade):
    faculdade = get_object_or_404(Faculdade, pk=id_faculdade)
    edt_faculdade = { 'faculdade':faculdade }
    return render(request, 'home/FACU_editar_faculdade.html', edt_faculdade)

@login_required(login_url="/login/")
def atualizar_faculdade(request):
    if request.method == 'POST':
        id_faculdade = request.POST['id_faculdade']
        fac = Faculdade.objects.get(pk=id_faculdade)
        fac.nome_faculdade = request.POST['nome_faculdade']
        fac.cnpj_faculdade = request.POST['cnpj_faculdade']
        fac.nome_direitor_faculdade = request.POST['nome_direitor_faculdade']
        fac.telefone_faculdade = request.POST['telefone_faculdade']
        fac.campus_faculdade = request.POST['campus_faculdade']
        fac.save()

        faculdades = Faculdade.objects.all()
        dados = {"faculdades":faculdades}
        return render(request,"home/FACU_dashboard.html",dados)
    else:
        return redirect("home/FACU_criar_faculdade.html")


