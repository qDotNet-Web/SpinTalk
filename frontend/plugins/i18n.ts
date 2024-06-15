import { createI18n } from 'vue-i18n'

const messages = {
  en: {
    welcome: 'Welcome',
    // Add more English translations here
  },
  de: {
    welcome: 'Willkommen',
    // Add more German translations here
  },
  fr: {
    welcome: 'Bienvenue',
    // Add more French translations here
  },
  // Add more locales here
}

export const i18n = createI18n({
  locale: 'en', // Set the initial locale
  fallbackLocale: 'en', // Set the fallback locale
  messages,
})