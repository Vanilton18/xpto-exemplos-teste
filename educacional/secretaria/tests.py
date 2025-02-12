import pytest
from datetime import date
from educacional.secretaria.models import Aluno
from django.db.utils import IntegrityError


@pytest.mark.django_db
class TestAlunoModel:

    def test_criar_aluno_valido(self):
        """Teste para verificar se um aluno válido é criado corretamente"""
        aluno = Aluno.objects.create(
            nome="João Silva",
            cpf="12345678901",
            matricula="2023001",
            data_nascimento=date(2005, 5, 15)
        )
        assert aluno.nome == "João Silva"
        assert aluno.cpf == "12345678901"
        assert aluno.matricula == "2023001"
        assert aluno.idade == date.today().year - 2005

