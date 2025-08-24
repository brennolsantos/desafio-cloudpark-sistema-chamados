<template>
    <div class="row justify-content-center mt-3">
        <h3 class="h3 col-12 text-center">Detalhes do Chamado - Editar</h3>
    </div>
    <div class="row justify-content-center mt-3">
        <div class="card col-lg-6 col-md-6 col-sm-6">
          <div class="card-body">
            <form @submit="editar()">
                <div class="card-body">
                    <div class="form-group mt-3 mt-3">
                        <label for="titulo" class="text-dark">Título</label>
                        <input type="text" class="form-control" id="titulo" v-model="chamado.titulo">
                    </div>
                    <div class="form-group mt-3">
                        <label for="descricao" class="text-dark">Descrição</label>
                        <textarea class="form-control" id="descricao" v-model="chamado.descricao"></textarea>
                    </div>
                    <div class="form-group mt-3">
                        <label for="prioridade" class="text-dark">Prioridade</label>
                        <select class="form-control" id="prioridade" v-model="chamado.prioridade">
                            <option value="Escolha uma prioridade" disabled selected>Escolha uma prioridade</option>
                            <option value="alta">Alta</option>
                            <option value="media">Média</option>
                            <option value="baixa">Baixa</option>
                        </select>
                    </div>
                    <div class="form-group mt-3">
                        <label for="status" class="text-dark">Status</label>
                        <select class="form-control" id="status" v-model="chamado.status">
                            <option value="Escolha um status" disabled selected>Escolha um status</option>
                            <option value="aberto">Aberto</option>
                            <option value="ematendimento">Em Atendimento</option>
                            <option value="resolvido">Resolvido</option>
                            <option value="cancelado">Cancelado</option>
                        </select>
                    </div>
                </div>
                <div class="form-group mt-3">
                    <label for="usuario" class="text-dark">Usuário</label>
                    <input type="text" class="form-control" id="usuario" v-model="usuario" readonly>
                    <input type="hidden" class="form-control" id="usuario" v-model="chamado.usuario" readonly>
                </div>
            </form>

            <button class="btn btn-primary mt-3" style="margin-right: 20px" @click="editar()">Salvar</button>
            <button class="btn btn-secondary mt-3" @click="$router.push('/home')">Cancelar</button> 
          </div>
        </div>
    </div>
</template>

<script>
import api from '../services/api';

export default {
    name: 'Edit',
    data: () => ({
        chamado: {},
        usuario: ''
    }),
    created() {
        this.fetchChamado();
    },
    methods: {
        async fetchChamado() {
            const id = this.$route.params.id;
            const response = await api.get(`/atendentes/api/chamados/${id}/`, {
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem('token')}`
                }
            });
            this.chamado = response.data;
            this.getUser(this.chamado.usuario);
        },

        editar(){
            const id = this.$route.params.id;
            api.put(`/atendentes/api/chamados/${id}/`, this.chamado, {
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem('token')}`
                }
            }).then(response => {
                window.alert('Chamado editado com sucesso!')
                this.$router.push('/home');
            }).catch(error => {
                console.error(error);
            });
        },
        getUser(id){
            api.get(`/autenticacao/api/usuarios/${id}/`, {
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem('token')}`
                }
            }).then(response => {
                this.usuario = response.data.username;
            }).catch(error => {
                console.error(error);
            });
        }
    }
}
</script>