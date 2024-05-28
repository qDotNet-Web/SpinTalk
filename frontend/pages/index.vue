<script setup lang="ts">
const route = useRoute()
import 'primevue/resources/themes/aura-dark-green/theme.css'
import '~/assets/css/primevue.css'
import '~/assets/css/style.css'
import 'primeicons/primeicons.css'

</script>

<template>
  <div class="main-app">
    <img class="main-logo" src="/img/logo_spintalk.png"/>
    <h1>Welcome to SpinTalk</h1>
    <LoginModal></LoginModal>
  </div>
</template>
