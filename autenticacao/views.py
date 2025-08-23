from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.views import View 
from django.shortcuts import render
from django.contrib.auth import get_user_model, logout

User = get_user_model()
class LoginView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'autenticacao/login.html')

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/atendentes/chamados/')
        return HttpResponseRedirect('/autenticacao/login/')
    
class RegisterView(View):

    def get(self, request, *args, **kwargs):
        context = {'error_message': None}
        return render(request, 'autenticacao/registrar.html', context)

    def post(self, request, *args, **kwargs):
        context = {}
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if username is None or username.strip() == '':
            context['error_message'] = 'Nome de usuário é obrigatório.'
            return render(request, 'autenticacao/registrar.html', context)

        if email is None or email.strip() == '':
            context['error_message'] = 'Email é obrigatório.'
            return render(request, 'autenticacao/registrar.html', context)

        if password != password2:
            context['error_message'] = 'As senhas não coincidem.'
            return render(request, 'autenticacao/registrar.html', context)
    

        if User.objects.filter(email=email).exists():
            context['error_message'] = 'Email já está em uso.'
            return render(request, 'autenticacao/registrar.html', context)

        user = User()
        user.email = email
        user.username = username
        user.tipo_user = 'atendente'
        user.set_password(password)
        user.save()

        return HttpResponseRedirect('/autenticacao/login/')
    


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect('/autenticacao/login/')