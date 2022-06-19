from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from sistemaSec.supervisor.models import Supervisor
from sistemaSec.sede.models import Sede

@login_required(login_url="/login/")
def criar_supervisor(request):
    if request.method == "POST":
        nome_supervisor = request.POST['nome_supervisor']
        email = request.POST['email']
        telefone = request.POST['telefone']
        
        sede_supervisor = request.POST['sede_supervisor']
        sede = Sede.objects.get(id_sede = sede_supervisor)
        supervisor = Supervisor.objects.create(nome_supervisor = nome_supervisor,
            email_supervisor = email, telefone_supervisor = telefone)
        
        supervisor.sede_supervisor.add(sede)
        supervisor.save()
        return redirect("/")
    else:
        return redirect("sistemaSec/templates/home/SUPE_criar_supervisor.html")

@login_required(login_url="/login/")
def consultar_supervisor(request):
    
    supervisores = Supervisor.objects.all()
    
    if 'buscar_supervisor' in request.GET:
        nome_consulta=request.GET['buscar_supervisor']

        if consultar_supervisor:
            lista_por_nome = supervisores.filter(Q(nome_supervisor__icontains=nome_consulta))
            
    dados = {"supervisores": lista_por_nome}
    return render(request,"home/SUPE_buscar_supervisor.html",dados)
    
@login_required(login_url="/login/")    
def editar_supervisor(request,id_supervisor):
    supervisor = get_object_or_404(Supervisor, pk=id_supervisor)
    sede = supervisor.sede_supervisor.all()

    editar_supervisor = { 'supervisor':supervisor,
                          'sede': sede }
    return render(request, 'home/SUPE_editar_supervisor.html', editar_supervisor)

@login_required(login_url="/login/")
def atualizar_supervisor(request):
    if request.method == 'POST':
        id_supervisor = request.POST['id_supervisor']
        sup = Supervisor.objects.get(pk=id_supervisor)
        sup.nome_supervisor = request.POST['nome_supervisor']
        sup.email_supervisor = request.POST['email']
        sup.telefone_supervisor = request.POST['telefone']

        sede_supervisor = request.POST['sede_supervisor']
        sede = Sede.objects.get(id_sede = sede_supervisor)
        sup.sede_supervisor.add(sede)
        sup.save()

        supervisores = Supervisor.objects.all()
        dados = {"supervisores":supervisores}
        return render(request,"home/SUPE_dashboard.html",dados)
    else:
        return redirect("home/SUPE_criar_supervisor.html")


