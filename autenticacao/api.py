from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'user': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class VerificarAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        response = False 

        if email:
            user = User.objects.filter(email=email).first()
            if user and user.tipo_user == 'tecnico':
                response = True 

        return Response({'status': response}, status=status.HTTP_200_OK)
