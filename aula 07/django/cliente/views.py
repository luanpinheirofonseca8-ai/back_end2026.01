from email.mime import text

from django.shortcuts import render
from django.http import HttpResponse



def ola_mundo(request):
    return HttpResponse("<h1>Olá, mundo!</h1>" "<p>Ola, djangooo!</p>")


def contato(request):
    return HttpResponse("<h1>Contato</h1>"
    "<form>" "<input type='text' placeholder='email@email.com'>" "<input type='text' placeholder='(21) 99999-9999'>" "<button type='submit'>Enviar</button>" "</form>")