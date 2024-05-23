// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ['nuxt-primevue'],
  primevue: {
    usePrimeVue: true,
    options: {
      unstyled: false
    },
    components: {
      include: '*',
    },
  },
  css: ['primevue/resources/themes/aura-dark-green/theme.css']
})