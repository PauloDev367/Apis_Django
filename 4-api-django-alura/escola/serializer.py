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

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    # diz que o campo curso vai ser do tipo de leitura e ele será representado pela descricao dele
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    
    def get_periodo(self, obj):
        return obj.get_periodo_display()

class ListaAlunosMatriculasSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_nome']