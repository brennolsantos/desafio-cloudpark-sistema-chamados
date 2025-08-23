from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
# Create your views here.

class ChamadosView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'atendentes/chamados.html')

class IndexView(View):

    def get(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return HttpResponseRedirect('/autenticacao/login/')

        return render(request, 'index.html')