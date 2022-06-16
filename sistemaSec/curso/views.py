from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from sistemaSec.curso.models import Curso


@login_required(login_url="/login/")
def criar_curso(request):
    if request.method == "POST":
        nome_curso = request.POST['nome_curso']
        
        curso = Curso.objects.create(nome_curso = nome_curso)
        
        curso.save()
        return redirect("/")
    else:
        return redirect("sistemaSec/templates/home/CUSO_criar_curso.html")

@login_required(login_url="/login/")
def consultar_curso(request):
    lista_por_curso=None
    curso = Curso.objects.all()
    
    if 'buscar_curso' in request.GET:
        curso_consulta=request.GET['buscar_curso']
        if consultar_curso:
            lista_por_curso= curso.filter(Q(nome_curso__icontains=curso_consulta))
    
    dados = {"cursos": lista_por_curso}
    return render(request,"home/CUSO_buscar_curso.html",dados)
    
@login_required(login_url="/login/")    
def editar_curso(request,id_curso):
    curso = get_object_or_404(Curso, pk=id_curso)
    edt_curso = { 'curso':curso }
    return render(request, 'home/CUSO_editar_curso.html', edt_curso)

@login_required(login_url="/login/")
def atualizar_curso(request):
    if request.method == 'POST':
        id_curso = request.POST['id_curso']
        cs = Curso.objects.get(pk=id_curso)
        cs.nome_curso = request.POST['nome_curso']
        cs.save()

        curso = Curso.objects.all()
        dados ={'cursos': curso}
        return render(request, 'home/CUSO_dashboard.html',dados)
    else:
        return redirect("home/CUSO_criar_curso.html")
