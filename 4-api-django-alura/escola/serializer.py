from rest_framework import serializers
from escola.models import Aluno, Curso


# Segue o mesmo principio dos ViewModel do C#, servem apenas para fazer a ponte do json
class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'