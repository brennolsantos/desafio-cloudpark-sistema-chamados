import { jwtDecode} from 'jwt-decode';
import api from './api';

export function signIn (email, password) {

    const response = api.post('/autenticacao/api/token/', {
        'email': email,
        'password': password
    }).then(res => {
        localStorage.setItem('token', res.data.access);
        localStorage.setItem('refresh', res.data.refresh);
        localStorage.setItem('user_email', email);
    });
}

export function signUp(email, usuario, password)
{
    const response = api.post('/autenticacao/api/registrar/', {
        'username': usuario,
        'email': email,
        'password': password,
        'tipo_user': 'tecnico'
    }).then(res => {
        console.log('OK');
    });
}

export function signOut () {
  localStorage.removeItem('token');
  localStorage.removeItem('refresh');
  localStorage.removeItem('user_email');
}

export function isSignedIn () {
  const token = localStorage.getItem('token');

  if (!token)     // Se não existe o token no LocalStorage
    return false; // significa que o usuário não está assinado.

  try {
    const { exp: expiration } = jwtDecode(token);
    const isExpired = !!expiration && Date.now() > expiration * 1000;

    if (isExpired)  // Se o token tem uma data de expiração e
      return false; // essa data é menor que a atual o usuário
                    // não está mais assinado.
    return true;
  } catch (_) {   // O "jwt-decode" lança erros pra tokens inválidos.
    return false; // Com um token inválido o usuário não está assinado.
  }
}