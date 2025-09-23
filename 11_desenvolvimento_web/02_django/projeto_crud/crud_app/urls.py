from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cadastrar/', views.cadastrar_pessoa, name='cadastrar_pessoa'),
    path('alterar/<int:id_pessoa>/', views.alterar_pessoa, name='alterar_pessoa'),
    path('excluir/<int:id_pessoa>/', views.excluir_pessoa, name='excluir_pessoa'),
    path('pesquisar/', views.pesquisar_pessoa, name='pesquisar_pessoa')
]