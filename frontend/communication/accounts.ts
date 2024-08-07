import axios from "axios";

axios.defaults.withCredentials = true;
const prefix: string = "http://localhost:8000/api/v1";

async function registerAccount(email: string, username: string, password: string) {
    axios.post(prefix+'/auth/register', {
        email: email,
        username: username,
        password: password,
        is_active: true,
        is_superuser: false,
        is_verified: false
    })
    .then((response) => console.log(response))
    .catch((error) => console.log(error));
}

async function loginAccount(email: string, password: string) {
    const formData = new FormData();
    formData.set('username', email);
    formData.set('password', password);

    try {
        const response = await axios.post(
            prefix+'/auth/jwt/login',
            formData,
            {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            }
        );
        if (response.status === 200) {
            let token = response.data.access_token;
            if (token){
                localStorage.setItem('token', token);
                return response.data.access_token;
            } else {
                return false;
            }
        }
    } catch (error) {
        console.log(error);
    }
}

async function logout() {
    try {
        const response = await axios.post('http://localhost:8000/auth/jwt/logout');
        console.log(response);
    } catch (error) {
        console.log(error);
    }
}

async function isAuthenticated() {
    try {
        const response = await axios.get('http://localhost:8000/auth/jwt/verify');
        console.log(response);
    } catch (error) {
    }
}

export { registerAccount, loginAccount, logout };