from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework import status

class AuthMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        full_url = request.build_absolute_uri()

        if request.user.is_authenticated and '/autenticacao/' in full_url and not 'logout' in full_url and not 'admin' in full_url:

            if request.user.tipo_user == 'atendente':
                return HttpResponseRedirect('/atendentes/chamados/')

        if '/api/' in full_url:
            if not request.user.is_authenticated and not 'token' in full_url and not 'registrar' in full_url:
                return HttpResponseRedirect('/')
            
            if request.user.is_authenticated and request.user.tipo_user != 'tecnico':
                return HttpResponseRedirect('/')

        return self.get_response(request)
