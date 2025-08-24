
import { createMemoryHistory, createRouter } from 'vue-router'
import { isSignedIn } from '../services/auth';
import Dashboard from '../components/Dashboard.vue';
import Login from '../components/Login.vue';
import Register from '../components/Register.vue';
import Edit from '../components/Edit.vue';


const routes = [
    {
      path: '/home',
      component: Dashboard,
      beforeEnter (_, __, next) { // Impede usuários não assinados
        if (isSignedIn()) {       // de acessar a página Home.
          next();
          return;
        }
        next('/login')
      }
    },
    {
      path: '/login',
      component: Login,
      beforeEnter (_, __, next) { // Impede usuários assinados de
        if (!isSignedIn()) {      // acessar a página de login.
          next();
          return;
        }
        next('/home')
      }
    },

    {
        path: '/register',
        component: Register,
        beforeEnter (_, __, next){
            if (isSignedIn()) {
                next('/home');
                return;
            }
            next();
        }
    },

    {
        path: '/edit/:id',
        component: Edit ,
        beforeEnter (_, __, next) { // Impede usuários não assinados
          if (isSignedIn()) {       // de acessar a página Home.
            next();
            return;
          }
          next('/login');
        }
    }
  ]

const router = createRouter({
  history: createMemoryHistory(),
  routes
})

export default router;