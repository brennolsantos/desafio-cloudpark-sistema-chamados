from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from .models import Chamado
from .serializers import ChamadoSerializer

class ChamadoAPIView(ModelViewSet):
    queryset = Chamado.objects.all()
    serializer_class = ChamadoSerializer

    