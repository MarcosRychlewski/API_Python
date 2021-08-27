from rest_framework import routers, serializers, viewsets
from localizacao.models import Localizacao


class LocalizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localizacao
        fields = ['id', 'linha1', 'linha2', 'cidade', 'estado', 'pais', 'latitude', 'longitude']