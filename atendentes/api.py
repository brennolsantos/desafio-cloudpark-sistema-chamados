from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from .models import Chamado
from .serializers import ChamadoSerializer

class ChamadoAPIView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            chamado = Chamado.objects.filter(id=id, usuario=request.user).first()
            if chamado:
                serializer = ChamadoSerializer(chamado)
                return Response({'chamado': serializer.data})
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        chamados = Chamado.objects.filter(usuario=request.user)
        serializer = ChamadoSerializer(chamados, many=True)
        print(f'CHAMADOS: {serializer.data}')
        return Response({'chamados': serializer.data})

    def post(self, request, *args, **kwargs):
        serializer = ChamadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(usuario=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        id = kwargs.get('id')
        try:
            chamado = Chamado.objects.get(id=id, usuario=request.user)
        except Chamado.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ChamadoSerializer(chamado, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        id = kwargs.get('id')
        try:
            chamado = Chamado.objects.get(id=id, usuario=request.user)
        except Chamado.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        chamado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)