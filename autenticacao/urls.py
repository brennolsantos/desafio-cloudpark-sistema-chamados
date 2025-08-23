from django.urls import path 
from .views import LoginView, RegisterView

app_name = 'autenticacao'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('registrar/', RegisterView.as_view(), name='registrar'),
]