from django.urls import path
from . import views

app_name = 'turma'

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('listar/', views.listar, name='listar'),
    path('registrar', views.registrar, name='registrar'),
    path('excluir/<int:numeroTurma>', views.excluir, name='excluir_turma')
]