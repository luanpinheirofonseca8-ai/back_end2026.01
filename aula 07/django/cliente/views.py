from email.mime import text

from django.shortcuts import render
from django.http import HttpResponse






def home(request):
    titulo = "Pagina Inicial"
    return render(request, 'clientes/home.html', {'titulo': titulo})
 
def dados_clientes(request):
    titulo = "Nosos Clientes"
    nossos_clientes = [
        {'nome': "Mario Silva de Carvalho", 'idade': '44 anos', 'nascimento': '17/08/1982'},
        {'nome': "Jose Alves", 'idade': '42 anos', 'nascimento': '17/08/1980'},
        {"nome": "Ana Maria Braga", "idade": 35, "nascimento": "10/12/1988"}
    ]
    return render(request, 'clientes/dados_clientes.html', {'titulo': titulo, 'dados_clientes':dados_clientes})
 
def formulario(request):
    titulo = "Nosos Clientes"
    return render(request, 'clientes/form.html', {'titulo':titulo})