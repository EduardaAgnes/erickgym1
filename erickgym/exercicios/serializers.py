from rest_framework.serializers import ModelSerializer
from .models import Alunos

class AlunoSerializer(ModelSerializer):
    class Meta:
        model = Alunos
        fields = ['id','nome', 'foto', 'sexo', 'dt_nasc', 'telefone', 'cpf']