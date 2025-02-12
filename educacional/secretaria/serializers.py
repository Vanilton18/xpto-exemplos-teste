from rest_framework import serializers
from .models import Aluno
from datetime import date


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'cpf', 'data_nascimento', 'matricula', 'data_registro', 'idade']
        read_only_fields = ['idade']

    def validate_cpf(self, value):
        if not value.isdigit() or len(value) != 11:
            raise serializers.ValidationError("O CPF deve ter exatamente 11 dígitos.")
        return value

    def validate_data_nascimento(self, value):
        idade = date.today().year - value.year
        if idade < 5:
            raise serializers.ValidationError("A idade mínima do aluno deve ser 5 anos.")
        return value
