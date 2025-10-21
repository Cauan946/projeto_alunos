from django.shortcuts import render, get_object_or_404, redirect
from .models import Aluno
from .forms import AlunoForm
from django.contrib import messages

def lista_alunos(request):
    alunos = Aluno.objects.order_by('-criado_em')
    context = {'alunos': alunos}
    return render(request, 'lista.html', context)

def aluno_create(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aluno criado com sucesso!')
            return redirect('lista_alunos')
    else:
        form = AlunoForm()
    return render(request, 'aluno_form.html', {'form': form})

def aluno_detail(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    return render(request, 'aluno_detalhe.html', {'aluno': aluno})

def aluno_update(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aluno atualizado com sucesso!')
            return redirect('lista_alunos')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'aluno_form.html', {'form': form})

def aluno_delete(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno.delete()
        messages.success(request, 'Aluno excluído com sucesso!')
        return redirect('lista_alunos')
    return render(request, 'aluno_confirm_delete.html', {'aluno': aluno})