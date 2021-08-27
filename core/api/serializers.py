from rest_framework import routers, serializers, viewsets
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from localizacao.api.serializers import LocalizacaoSerializer
from rest_framework.fields import SerializerMethodField


class PontoTuristicoSerializer(serializers.ModelSerializer):

    #atracoes = AtracaoSerializer(many=True)
    #localizacao = LocalizacaoSerializer()
    #descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao']

    # def get_descricao_completa(self, obj):
    #     return '%s - %s ' % (obj.nome, obj.descricao)
