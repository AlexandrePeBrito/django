from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from sistemaSec.edital.models import Edital
from sistemaSec.programa.models import Programa

@login_required(login_url="/login/")
def criar_edital(request):
    if request.method == "POST":
        id_edital = request.POST['id_edital']
        quantidade_vagas = request.POST['quantidade_vagas']
        prog = request.POST['programa']
        
        programa = Programa.objects.get(id_programa=prog)
        edital = Edital.objects.create(id_edital = id_edital,
            quantidade_vagas_edital = quantidade_vagas,
            id_programa_edital = programa)
        
        edital.save()
        return redirect("/")
    else:
        return redirect("sistemaSec/templates/home/EDTL_criar_edital.html")

@login_required(login_url="/login/")
def consultar_edital(request):
    lista_por_edital=None
    edital = Edital.objects.all()
    
    if 'buscar_edital' in request.GET:
        edital_consulta=request.GET['buscar_edital']
        programa_consulta=request.GET['buscar_programa']
        if consultar_edital:
            lista_por_edital = edital.filter(Q(id_edital__icontains=edital_consulta))
            listar_por_programa = lista_por_edital.filter(Q(id_programa_edital__nome_programa__icontains=programa_consulta))
    
    dados = {"editais": listar_por_programa}
    return render(request,"home/EDTL_buscar_edital.html",dados)
    
@login_required(login_url="/login/")    
def editar_edital(request,id_edital):
    edital = get_object_or_404(Edital, pk=id_edital)
    edt_edital = { 'edital':edital }
    return render(request, 'home/EDTL_editar_edital.html', edt_edital)

@login_required(login_url="/login/")
def atualizar_edital(request):
    if request.method == 'POST':
        cod_edital = request.POST['id_edital']
        edt = Edital.objects.get(pk=cod_edital)
        edt.id_edital= cod_edital
        edt.quantidade_vagas_edital = request.POST['quantidade_vagas']
       
        prog = request.POST['programa']
        programa = Programa.objects.get(id_programa=prog)
        edt.id_programa_edital = programa
        edt.save()

        editais = Edital.objects.all()
        dados ={'editais': editais}
        return render(request, 'home/EDTL_dashboard.html',dados)
    else:
        return redirect("home/EDTL_criar_edital.html")
