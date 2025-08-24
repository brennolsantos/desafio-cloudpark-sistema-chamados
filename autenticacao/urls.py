from django.urls import path 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import LoginView, RegisterView, LogoutView
from .api import RegisterAPIView

app_name = 'autenticacao'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('registrar/', RegisterView.as_view(), name='registrar'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/registrar/', RegisterAPIView.as_view(), name='api_registrar'),
]