from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula


# Segue o mesmo principio dos ViewModel do C#, servem apenas para fazer a ponte do json
class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'
        # exclude = ['id']