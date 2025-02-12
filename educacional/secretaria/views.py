from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Aluno
from .serializers import AlunoSerializer


class AlunoListCreateAPIView(APIView):
    """
    View para listar e registrar alunos, com suporte a filtros por matrícula e CPF.
    """

    def get(self, request):
        matricula = request.query_params.get('matricula')
        cpf = request.query_params.get('cpf')

        # Filtro condicional
        if matricula:
            alunos = Aluno.objects.filter(matricula=matricula)
        elif cpf:
            alunos = Aluno.objects.filter(cpf=cpf)
        else:
            alunos = Aluno.objects.all()

        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)