from django.shortcuts import render
from .models import Cliente ,Curso, Campus
# Create your views here.


def home(request):
    return render(request, 'alunos/home.html')




def info(request):

    titulo = 'Informações dos Alunos' 

    alunos = Cliente.objects.all()
    
    return render(request, 'alunos/inscricao.html', {'msg': titulo,'alunos': alunos})

def formulario(request):
    titulo = "Nossos Clientes"
    return render(request, 'clientes/formulario.html', {'titulo':titulo})



def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'alunos/cursos.html', {'cursos': cursos})    



def campus(request):
    campus = Campus.objects.all()
    return render(request, 'alunos/campus.html', {'campus': campus})