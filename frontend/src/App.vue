<template>
 <div class="container"><router-view></router-view></div>
</template>

<script>
export default {
  name: 'App',
  mounted(){
    if(localStorage.getItem('token')){
      this.$router.push('/home');
    } else {
      this.$router.push('/login');
    }
  }
}
</script>