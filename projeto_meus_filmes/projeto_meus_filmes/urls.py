
from django.contrib import admin
from django.urls import path
from meus_filmes import views
from usuarios import views as usuario_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('conta/',usuario_views.novo_usuario, name='novo_usuario'),
    path('login/',auth_views.LoginView.as_view(template_name='usuarios/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='usuarios/logout.html'),name='logout'),
    path('',views.pagina_inicial,name='pagina_inicial'),
    path('novo_filme/',views.criar,name='novo_filme'),
    path('<int:id_filme>',views.detalhe,name='detalhe'),
    path('novo_filme/<int:id_filme>',views.editar,name='editar'),
    path('excluir_filme/<int:id_filme>',views.excluir,name='excluir'),
]
