from django.urls import path 
from .views import ChamadosView

app_name = 'atendentes'

urlpatterns = [
    path('chamados/', ChamadosView.as_view(), name='chamados'),
]