from rest_framework import serializers
from .models import Chamado

class ChamadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chamado
        required_fields = ['titulo', 'prioridade', 'status']
        fields = ['id', 'titulo', 'descricao', 'prioridade', 'status', 'data_criacao', 'usuario']
        read_only_fields = ['id', 'data_criacao', 'usuario']