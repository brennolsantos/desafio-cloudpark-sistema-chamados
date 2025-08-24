from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChamadosView, ChamadosCadastroView, ChamadosEditView, CadastroDeleteView
from .api import ChamadoAPIView

app_name = 'atendentes'

router = DefaultRouter()
router.register(r'chamados', ChamadoAPIView, basename='api_chamados')

urlpatterns = [
    path('chamados/', ChamadosView.as_view(), name='chamados'),
    path('chamados/<int:id>/', ChamadosView.as_view(), name='chamados_detail'),
    path('chamados/<int:id>/editar/', ChamadosEditView.as_view(), name='chamados_editar'),
    path('chamados/<int:id>/deletar/', CadastroDeleteView.as_view(), name='chamados_deletar'),
    path('chamados/novo/', ChamadosCadastroView.as_view(), name='chamados_novo'),
    path('api/', include(router.urls))
]