from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .models import Chamado
# Create your views here.

class ChamadosView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        context = {}
        status = request.GET.get('status')  
        
        if request.user.is_authenticated == False:
            return HttpResponseRedirect('/autenticacao/login/')
        
        if request.user.tipo_user != 'atendente':
            return HttpResponseRedirect('/autenticacao/login/')

        if id is not None:
            try:
                chamado = Chamado.objects.get(id=id)
                if chamado.usuario != request.user:
                    return HttpResponseRedirect('/atendentes/chamados/')
            except Chamado.DoesNotExist:
                return HttpResponseRedirect('/atendentes/chamados/')
            
            context['chamado'] = chamado
            return render(request, 'atendentes/chamados_id.html', context)

        chamados = Chamado.objects.filter(usuario=request.user)

        if status:
            chamados = chamados.filter(status=status)

        if chamados.exists():
            context['chamados'] = chamados
        else:
            context['chamados'] = []

        return render(request, 'atendentes/chamados.html', context)

class ChamadosEditView(View):

    def get(self, request, *args, **kwargs):
        context = {}
        id = kwargs.get('id')   
        try:
            chamado = Chamado.objects.get(id=id, usuario=request.user)
            context['chamado'] = chamado
        except Chamado.DoesNotExist:
            return HttpResponseRedirect('/atendentes/chamados/')

        return render(request, 'atendentes/chamados_editar.html', context)

    def post(self, request, *args, **kwargs):
        context = {}
        id = kwargs.get('id')

        chamado = Chamado.objects.get(id=id, usuario=request.user)

        if not chamado:
            return HttpResponseRedirect('/atendentes/chamados/')

        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        prioridade = request.POST.get('prioridade')
        setor = request.POST.get('setor')
        status = request.POST.get('status')

        print(request.POST)

        if None in [titulo, descricao, prioridade, setor, status] or '' in [titulo, descricao, prioridade, setor, status]:
            context['error_message'] = 'Todos os campos são obrigatórios.'
            return render(request, 'atendentes/chamados_editar.html', context)

        chamado.titulo = titulo
        chamado.descricao = descricao
        chamado.prioridade = prioridade
        chamado.setor = setor
        chamado.status = status
        chamado.save()

        return HttpResponseRedirect(f'/atendentes/chamados/{chamado.id}/')

class ChamadosCadastroView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'atendentes/chamados_cadastro.html', context)

    def post(self, request, *args, **kwargs):
        context = {}
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao') 
        prioridade = request.POST.get('prioridade') 
        setor = request.POST.get('setor') 
        status = request.POST.get('status')

        if status is None or status.strip() == '':
            status = 'aberto'

        if None in [titulo, status, prioridade] or '' in [titulo, status, prioridade]:
            context['error_message'] = 'Título, Prioridade e Status são obrigatórios.'  
            return render(request, 'atendentes/chamados.html', context)

        if status == 'resolvido' and request.user.tipo_user == 'atendente':
            context['error_message'] = 'Atendentes não podem criar chamados com status "Resolvido".'
            return render(request, 'atendentes/chamados.html', context)
        
        chamado = Chamado()
        chamado.usuario = request.user
        chamado.titulo = titulo
        chamado.descricao = descricao
        chamado.prioridade = prioridade
        chamado.setor = setor
        chamado.status = status
        chamado.save()

        return HttpResponseRedirect('/atendentes/chamados/')
 

class CadastroDeleteView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        id = kwargs.get('id')

        try:
            chamado = Chamado.objects.get(id=id, usuario=request.user)
            chamado.delete()
        except Chamado.DoesNotExist:
            return HttpResponseRedirect('/atendentes/chamados/')

        return HttpResponseRedirect('/atendentes/chamados/')

class IndexView(View):

    def get(self, request, *args, **kwargs):

        if not request.user.is_authenticated or request.user.tipo_user != 'atendente':
            return HttpResponseRedirect('/autenticacao/login/')

        return render(request, 'index.html')