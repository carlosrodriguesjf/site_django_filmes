from django.shortcuts import render
from django.shortcuts  import HttpResponse

def pagina_inicial(request):
    return HttpResponse('Meus livros')

def contato(request):
    return HttpResponse('Em caso de dúvidas, envie um e-mail para contato@suporte.com')
