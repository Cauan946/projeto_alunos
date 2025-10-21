from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_alunos, name='lista_alunos'),
    path('novo/', views.aluno_create, name='aluno_create'),
    path('<int:pk>/', views.aluno_detail, name='aluno_detail'),
    path('<int:pk>/editar/', views.aluno_update, name='aluno_update'),
    path('<int:pk>/excluir/', views.aluno_delete, name='aluno_delete'),
]