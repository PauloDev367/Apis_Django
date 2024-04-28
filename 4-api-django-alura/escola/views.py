from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import CursoSerializer, AlunoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculasSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    
# Viewsets incluem ações como criar, listar, atualizar ou deletar.
# A utilização de Viewset pode evitar repetir a lógica das views.
class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
class MatriculasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matrículas de um aluno"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer
    
class ListarAlunosMatriculados(generics.ListAPIView):
    """Listando alunos matriculados"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculasSerializer