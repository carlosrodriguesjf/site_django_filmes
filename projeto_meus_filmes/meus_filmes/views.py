from django.shortcuts import render,redirect, HttpResponse
from .models import Filme
from .forms import FilmeForm



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


def detalhe(request,id_filme):
    dados = {
        'dados': Filme.objects.get(pk=id_filme)
    }
    return render(request,'filmes/detalhe.html',dados)


def criar(request):
    if request.method =='POST':
        filme_form = FilmeForm(request.POST)
        if filme_form.is_valid():
            filme_form.save()
        return redirect('pagina_inicial')
    else:
        filme_form = FilmeForm()
        formulario = {
            'formulario': filme_form
        }
    return render(request,'filmes/novo_filme.html',context=formulario)


def editar(request,id_filme):
    filme = Filme.objects.get(pk=id_filme)
    #caso a requisição seja GET
    if request.method == 'GET':
        formulario = FilmeForm(instance=filme)
        return render(request,'filmes/novo_filme.html', {'formulario': formulario})
    # caso a requisição seja POST
    else:
        formulario = FilmeForm(request.POST, instance=filme)
        if formulario.is_valid():
            formulario.save()
        return redirect('pagina_inicial')

def excluir(request,id_filme):
    filme = Filme.objects.get(pk=id_filme)
    if request.method == 'POST':
        filme.delete()
        return redirect('pagina_inicial') 
    return render(request,'filmes/confirmar_exclusao.html',{'item': filme})





