from email.mime import text

from django.shortcuts import render
from django.http import HttpResponse



def ola_mundo(request):
    return HttpResponse("<h1>Olá, mundo!</h1>" "<p>Ola, djangooo!</p>")


def contato(request):
    return HttpResponse("<h1>Contato</h1>  <form>  <input type=text placeholder=email@email.com>  <input text=text placeholder=(21)99999-9999> <button>enviar</button> </form>") 



#aula 08
def formulario(request):
    return render (request, "clientes/formulario.html")

def home(request):
    #Conceito de context (contexto)
    #Context - pega dados na view e passa para o template
 
    titulo = "Nossos melhores clientes "
 
    nosso_cliente = {
        'nome': "Thyago Assis de Almeida",
        'idade': 44,
        'nascimento': "15/021982"
    }
 
    nomes_clientes = ["Maria", "Joao", "Mateus", "Ana", "Marcos"]
 
    carros = [
        {'marca': "Chevrolet", 'modelo':'Onix LT', 'ano': '2020'},
        {'marca': "Fiat", 'modelo':'Uno', 'ano': '2010'},
        {'marca': "VW", 'modelo':'Gol', 'ano': '2022'},
    ]
 
    return render(request, "clientes/home.html", {'msg':titulo, 'lista_clientes':nosso_cliente, 'dados':nomes_clientes, 'meus_carros':carros})
 
def formulario(request):
    return render(request, "clientes/formulario.html" )