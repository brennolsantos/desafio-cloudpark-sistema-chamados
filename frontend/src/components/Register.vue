<template>
    <div class="row justify-content-center mt-3">
        <h3 class="h3 col-12 text-center">Sistema de Chamados - Técnicos</h3>
    </div>
   <div class="row justify-content-center mt-3">
    <form @submit.prevent="onSubmit()" class="col-lg-6 col-md-12 col-sm-12">
        <div class="mb-3">
        <label for="email" class="form-label">Email</label>
        <input type="email" class="form-control" id="email" v-model="email" required>
        </div>
        <div class="mb-3">
            <label for="usuario" class="form-label">Usuário</label>
            <input type="text" class="form-control" id="usuario" v-model="usuario" required>
        </div>
        <div class="mb-3">
        <label for="password" class="form-label">Senha</label>
        <input type="password" class="form-control" id="password" v-model="password" required>
        </div>
        <div class="mb-3">
            <label for="confirmPassword" class="form-label">Confirmar Senha</label>
            <input type="password" class="form-control" id="confirmPassword" v-model="confirmPassword" required>
        </div>
        <button type="submit" class="btn btn-primary">Registrar</button>
        <button type="button" class="btn btn-secondary" style="margin-left: 20px;" @click="goBack()">Voltar</button>
    </form>
   </div>
</template>

<script>
import {signUp} from '../services/auth';

export default {
    name: 'Register',
    data() {
        return {
            email: '',
            usuario: '',
            password: '',
            confirmPassword: ''
        };
    },
    methods: {
        onSubmit(){
            if(this.password !== this.confirmPassword) {
                alert("As senhas não conferem.");
                return;
            }

            signUp(this.email, this.usuario, this.password);
            this.$router.push('/login');
        }
    }
}
</script>