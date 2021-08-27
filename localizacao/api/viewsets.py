from rest_framework import routers, serializers, viewsets
from localizacao.api.serializers import LocalizacaoSerializer
from localizacao.models import Localizacao


class LocalizacaoViewSet(viewsets.ModelViewSet):
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer