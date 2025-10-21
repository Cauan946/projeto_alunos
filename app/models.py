from django.db import models
from django.urls import reverse

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=8, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('aluno_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'