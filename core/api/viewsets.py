from rest_framework import routers, serializers, viewsets, status
from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.templatetags.rest_framework import data


class PontoTuristicoViewSet(viewsets.ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    #permission_classes = [IsAdminUser] = Se voce quiser que sua rota seja acessada apenas pelo admin
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = PontoTuristico.objects.all()

    # @api_view(['GET'])
    # def list(request):
    #     pont = PontoTuristico.objects.all()
    #     serializer = PontoTuristicoSerializer(pont, many=True)
    #     return Response(serializer.data)
    #
    # @api_view(['POST'])
    # def post(request, pk):
    #     serializer = PontoTuristicoSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
