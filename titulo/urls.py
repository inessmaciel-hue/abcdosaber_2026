from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('teste/', views.teste, name='teste'),
    path('show_view/', views.show_views, name='show_views'),
    path('listar_exemplo/', views.listar_exemplo, name='listar_exemplo'),
    path('abc/', views.abc, name='abc'),
    path('aluno/', views.aluno, name='aluno'),
    path('instrutor/', views.instrutor, name='instrutor'),
    path('tipo_de_atividade/', views.tipo_de_atividade, name='tipo_de_atividade'),
    path('turma/', views.turma, name='turma'),
    path('utilitarios/', views.utilitarios, name='utilitarios'),
]