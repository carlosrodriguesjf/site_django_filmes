"""
URL configuration for projeto_meus_filmes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from meus_filmes import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.pagina_inicial,name='pagina_inicial'),
    path('novo_filme/',views.criar,name='novo_filme'),
    path('filme_registrado/',views.filme_registrado,name='filme_registrado'),
    path('/<int:id_filme>',views.detalhe,name='detalhe'),
    path('novo_filme/<int:id_filme>',views.editar,name='editar'),
    path('excluir_filme/<int:id_filme>',views.excluir,name='excluir'),
    

]
