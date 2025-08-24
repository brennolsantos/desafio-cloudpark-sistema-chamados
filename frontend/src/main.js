import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// Criar a app primeiro
const app = createApp(App)

// Depois usar os plugins
app.use(router)
// Só então montar
app.mount('#app')

console.log('Vue app initialized successfully')