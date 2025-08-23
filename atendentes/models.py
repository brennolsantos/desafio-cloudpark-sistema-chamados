from django.db import models

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

    def __str__(self):
        return f'({self.id}) {self.titulo} - {self.status} - {self.prioridade}'

    class Meta:
        verbose_name = 'Chamado'
        verbose_name_plural = 'Chamados'
        ordering = ['-id']