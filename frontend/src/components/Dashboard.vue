<template>
  <div class="row justify-content-center mb-3 mt-3">
    <h3 class="h3 text-center text-dark">Sistema de Chamados - Técnicos</h3>
  </div> 
  <div class="row-justify-content-center">
    <h3 class="h3 col-12 text-center mt-3">Dashboard - Chamados</h3>
    <div class="col-12 text-end mb-3">
        <label for="filtro-status" class="text-center" style="margin-right: 10px;">Filtrar por Status:</label>
        <select @change="filtrarStatus" id="filtro-status" style="margin-right: 30px;" v-model="filtroStatus">
            <option value="">Todos</option>
            <option value="aberto">Aberto</option>
            <option value="ematendimento">Em Atendimento</option>
            <option value="resolvido">Resolvido</option>
            <option value="cancelado">Cancelado</option>
        </select>
        <button class="btn btn-success" @click="refreshChamados" style="margin-right: 40px;">Atualizar Lista</button>
        <button class="btn btn-danger" @click="signOut(); $router.push('/login')">Sair</button>
    </div>
    <div class="col-12">
        <table class="table table-striped">
            <thead>
                <tr>
                    <th scope="col">ID</th>
                    <th scope="col">Título</th>
                    <th scope="col">Descrição</th>
                    <th scope="col">Setor</th>
                    <th scope="col">Prioridade</th>
                    <th scope="col">Status</th>
                    <th scope="col">Data de Criação</th>
                    <th scope="col">Ações</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="chamado in chamados" :key="chamado.id">
                    <th scope="row">{{ chamado.id }}</th>
                    <td>{{ chamado.titulo }}</td>
                    <td>{{ chamado.descricao }}</td>
                    <td>{{ setores[chamado.setor] }}</td>
                    <td :class="'text-' + cores[chamado.prioridade]">{{ prioridades[chamado.prioridade] }}</td>
                    <td>{{ status[chamado.status] }}</td>
                    <td>{{ new Date(chamado.data_criacao).toLocaleString() }}</td>
                    <td>
                        <button class="btn btn-primary" @click="editChamado(chamado.id)">Editar</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import api from '../services/api';
import { signOut } from '../services/auth';

export default {
    name: 'Dashboard',
    data: () => ({
        chamados: [],
        prioridades: {
            'alta': 'Alta',
            'media': 'Média',
            'baixa': 'Baixa'    
        },
        cores: {
            'alta': 'danger',
            'media': 'warning',
            'baixa': 'success'
        },
        textos: {
            'alta': 'white',
            'media': 'dark',
            'baixa': 'dark'
        },
        status: {
            'aberto' : 'Aberto',
            'ematendimento': 'Em Atendimento',
            'resolvido': 'Resolvido',
            'cancelado': 'Cancelado'
        },
        setores: {
            'TI': 'TI',
            'financeiro': 'Financeiro',
            'atendimento': 'Atendimento',
            'rh': 'Recursos Humanos',
            'tecnico': 'Técnico',
            'marketing': 'Marketing'
        },
        filtroStatus: ""
    }),
    created() {
        const email = localStorage.getItem('user_email');
        const response = api.post(`/autenticacao/api/verificar/`,{
            'email': email
        }).
        then(res => {
            console.log('TECNICO: ', res.data);
            if(!res.data.status)
            {
                window.alert('Sistema apenas para técnicos. Você será redirecionado para a página de login.');
                signOut();
                this.$router.push('/login');
            }
        });

        this.filtroStatus = "";
        this.fetchChamados();
    },
    methods: {
        async fetchChamados() {
            const response = await api.get('/atendentes/api/chamados/', {
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem('token')}`
                }
            });
            this.chamados = response.data;

        },
        editChamado(id){
            this.$router.push(`/edit/${id}`);
        },
        refreshChamados(){
            this.fetchChamados();
        },
        signOut(){
            localStorage.removeItem('token');
            localStorage.removeItem('user_email');
            this.$router.push('/login');
        },
        filtrarStatus(){
            this.fetchChamados().then(() => {
                if(this.filtroStatus === ""){
                    return;
                }

                this.chamados = this.chamados.filter(chamado => chamado.status === this.filtroStatus);
            });
        }
    }
}
</script>