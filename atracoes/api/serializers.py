from rest_framework import routers, serializers, viewsets
from atracoes.models import Atracao


class AtracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atracao
        fields = ['id', 'nome', 'endereco', 'descricao', 'horario', 'tipo']