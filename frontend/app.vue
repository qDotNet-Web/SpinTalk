<template>
  <div>
  </div>
  <Toast />
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>


<script>
import 'primevue/resources/themes/aura-dark-green/theme.css'
import '~/assets/css/primevue.css'
import '~/assets/css/style.css'
import 'primeicons/primeicons.css'
import {connect, disconnect, send} from '~/communication/websockets.ts'
</script>
