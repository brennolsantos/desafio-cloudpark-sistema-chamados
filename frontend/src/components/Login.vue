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
        <label for="password" class="form-label">Senha</label>
        <input type="password" class="form-control" id="password" v-model="password" required>
        </div>
        <button type="submit" class="btn btn-primary">Logar</button>
        <button type="button" class="btn btn-secondary" style="margin-left: 20px;" @click="goSignUp()">Registrar</button>
    </form>
   </div>
</template>

<script>
  import { signIn } from '../services/auth';
  export default {
    methods: {
      async onSubmit () {
          signIn(this.email, this.password);
          this.$router.push('/home');
      },
      goSignUp() {
        this.$router.push('/register');
      }
    }
  };
</script>