from rest_framework import routers, serializers, viewsets
from comentarios.models import Comentario


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id', 'usuario', 'comentario', 'data', 'aprovado']