from django.shortcuts import render
from django.shortcuts  import HttpResponse
from .models import Filme



def pagina_inicial(request):
    dados = {
        'dados': Filme.objects.all()
    }
    return render(request,'filmes/pagina_inicial.html',context=dados)

def novo_filme(request):
    return render(request,'filmes/novo_filme.html')

def filme_registrado(request):
    filme = {
        'genero_filme': request.POST.get('GeneroFilme')
    }
    return render(request,'filmes/filme_registrado.html',filme)




