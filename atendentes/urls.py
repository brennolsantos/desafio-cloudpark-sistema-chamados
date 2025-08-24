from django.urls import path 
from .views import ChamadosView, ChamadosCadastroView, ChamadosEditView, CadastroDeleteView
from .api import ChamadoAPIView

app_name = 'atendentes'

urlpatterns = [
    path('chamados/', ChamadosView.as_view(), name='chamados'),
    path('chamados/<int:id>/', ChamadosView.as_view(), name='chamados_detail'),
    path('chamados/<int:id>/editar/', ChamadosEditView.as_view(), name='chamados_editar'),
    path('chamados/<int:id>/deletar/', CadastroDeleteView.as_view(), name='chamados_deletar'),
    path('chamados/novo/', ChamadosCadastroView.as_view(), name='chamados_novo'),
    path('api/chamados/', ChamadoAPIView.as_view(), name='api_chamados'),
    path('api/chamados/<int:id>/', ChamadoAPIView.as_view(), name='api_chamado_detail')
]