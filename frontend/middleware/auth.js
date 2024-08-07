export default async function ({ $axios, redirect }) {
  const token = localStorage.getItem('token');
  if (!token) {
    return redirect('/login');
  }

  try {
    await $axios.get('/auth/validate-token');
  } catch (error) {
    // Token ist ungültig oder abgelaufen
    localStorage.removeItem('token');
    return redirect('/login');
  }
}
