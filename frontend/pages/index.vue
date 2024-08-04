<template>
  <div class="main-app">
     <div class="main-logo">
        <img src="/img/logo_spintalk.png" alt="logo" />
     </div>
    <h1>Welcome to SpinTalk</h1>
    <LoginModal></LoginModal>
  </div>
</template>

<script setup lang="ts">
const route = useRoute()
import '~/assets/css/primevue.css'
import '~/assets/css/style.css'
import 'primeicons/primeicons.css'

</script>