from django.shortcuts import render
from app.models import Aluno

def lista_alunos(request):
    alunos = Aluno.objects.order_by('-criado_em')
    context = {'alunos': alunos}
    return render(request, 'lista.html', context)
