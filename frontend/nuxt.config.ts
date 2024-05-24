// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: {
    enabled: true,

    timeline: {
      enabled: true,
    },
  },
  modules: ['nuxt-primevue', 'usebootstrap'],

  primevue: {
    cssLayerOrder: 'bootstrap, primevue',
    usePrimeVue: true,
    options: {
      unstyled: false
    },
    components: {
      include: '*',
    },
  },
  css: ['primevue/resources/themes/aura-dark-green/theme.css',
  ],
  vue: {
    propsDestructure: true
  },
  app: {
    pageTransition: { name: 'page', mode: 'out-in' }
  },
})