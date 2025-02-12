# models.py
from django.db import models
from datetime import date


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    matricula = models.CharField(max_length=20, unique=True)
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    @property
    def idade(self):
        hoje = date.today()
        return hoje.year - self.data_nascimento.year - (
                (hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day)
        )
