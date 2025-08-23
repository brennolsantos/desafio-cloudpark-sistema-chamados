from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Chamado(models.Model):
    PRIORIDADE_CHOICES = (
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    )

    titulo = models.CharField(max_length=200, null=False, blank=False)
    descricao = models.TextField(null=True, blank=True)
    prioridade = models.CharField(max_length=10, choices=PRIORIDADE_CHOICES, null=False, blank=False)
    setor = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('aberto', 'Aberto'), ('fechado', 'Fechado')], null=False, blank=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chamados', null=True)

    def __str__(self):
        return f'({self.id}) {self.titulo} - {self.status} - {self.prioridade}'

    class Meta:
        verbose_name = 'Chamado'
        verbose_name_plural = 'Chamados'
        ordering = ['-id']