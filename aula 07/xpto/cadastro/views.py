from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'alunos/home.html')




def info(request):

    titulo = 'Informações dos Alunos' 

    alunos = [
        {'nome': 'João', 'curso': 'Python', 'turma': 'A'},
        {'nome': 'Maria', 'curso': 'JavaScript', 'turma': 'B'},
        {'nome': 'Pedro', 'curso': 'Java', 'turma': 'C'},
    ]


    return render(request, 'alunos/inscricao.html', {'msg': titulo,'alunos': alunos})