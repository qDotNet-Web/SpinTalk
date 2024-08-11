export default async function ({ $axios, redirect }) {
  console.log('Middleware auth.js');
  const token = localStorage.getItem('token');
  if (!token) {
    return redirect('/');
  }

  try {
    await $axios.get('http://localhost:8000/api/v1/auth/validate-token');
  } catch (error) {
    // Token ist ungültig oder abgelaufen
    localStorage.removeItem('token');
    return redirect('/');
  }
}
