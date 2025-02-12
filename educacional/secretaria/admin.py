from django.contrib import admin
from .models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'matricula', 'data_nascimento', 'data_registro', 'idade')
    search_fields = ('nome', 'cpf', 'matricula')
    list_filter = ('data_registro',)
    ordering = ('nome',)
    readonly_fields = ('idade',)