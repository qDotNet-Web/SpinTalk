<style scoped></style>
<template>
    <Button label="Getting Started" icon="pi pi-user" outlined @click="register_visible = true" />
    <Dialog v-model:visible="register_visible" modal :pt="{
        root: 'border-none',
        mask: {
            style: 'backdrop-filter: blur(2px)'
        }
    }">
        <template #container="{ closeCallback }">
            <div v-focustrap class="flex-column px-5 py-5 gap-4"
                style="border-radius: 12px; background-color: var(--main-modal-bg); width: 350px;">
                <div class="gap-2 mb-pi" style="justify-content: center; display: flex;">
                    <div class="iconBox" style="display: inline-flex;">
                        <img src="/img/logo_spintalk.png" style="width: 60px;" />
                    </div>
                </div>
                <div class="inline-flex flex-column gap-2 mb-3" style="text-align: center;">
                    <h3 class="modal-title" id="createLobbyModalLabel">Start your Journey</h3>
                </div>
                <div class="inline-flex flex-column gap-2 mb-3">
                    <FloatLabel class="ip_float">
                        <InputText v-tooltip.top="'Enter your username'" id="ip_username" name="ip_userName"
                            v-model="ip_userName" class="w-full ip_float bg-white-alpha-20" maxlength="35" autofocus />
                        <label for="ip_userName">Username</label>
                    </FloatLabel>
                </div>
                <div class="inline-flex flex-column gap-2 mb-3">
                    <FloatLabel class="ip_float">
                        <InputText v-tooltip.top="'Enter your mail'" id="ip_mail" name="ip_mail" v-model="ip_mail"
                            class="w-full ip_float bg-white-alpha-20" maxlength="35" />
                        <label for="ip_mail">E-Mail</label>
                    </FloatLabel>
                </div>
                <div class="inline-flex flex-column gap-2 mb-1">
                    <FloatLabel class="ip_float">
                        <InputText v-tooltip.top="'Enter your password'" id="ip_password" name="ip_password"
                            v-model="ip_password" class="w-full ip_float bg-white-alpha-20" maxlength="35" />
                        <label for="ip_password">Password</label>
                    </FloatLabel>
                </div>
                <div class="flex-terms flex-column gap-2 mb-2">
                    <p class="p-terms">Accept Terms & Conditions</p>
                    <InputSwitch v-model="checkedTerms" />
                </div>
                <div class="flex-modal align-items-center gap-3">
                    <Button label="Cancel" @click="closeCallback" text
                        class="p-3 w-full text-primary-50 border-1 border-white-alpha-30 hover:bg-white-alpha-10"
                        outlined></Button>
                    <Button label="Start" @click="closeCallback, register()" text
                        class="p-3 w-full text-primary-50 border-1 border-white-alpha-30 hover:bg-white-alpha-10"
                        outlined :disabled="!checkedTerms"></Button>
                </div>
                <div style="text-align: center; margin-top: 1rem;">
                    <p class="p-terms">Already have an account?</p>
                    <Button label="Login" @click="register_visible = false; login_visible = true;" text class="text-primary-50"></Button>
                </div>
            </div>
        </template>
    </Dialog>

    <Dialog v-model:visible="login_visible" modal :pt="{
        root: 'border-none',
        mask: {
            style: 'backdrop-filter: blur(2px)'
        }
    }">
        <template #container="{ closeCallback }">
            <div v-focustrap class="flex-column px-5 py-5 gap-4"
                style="border-radius: 12px; background-color: var(--main-modal-bg); width: 350px;">
                <div class="gap-2 mb-pi" style="justify-content: center; display: flex;">
                    <div class="iconBox" style="display: inline-flex;">
                        <img src="/img/logo_spintalk.png" style="width: 60px;" />
                    </div>
                </div>
                <div class="inline-flex flex-column gap-2 mb-3" style="text-align: center;">
                    <h3 class="modal-title" id="createLobbyModalLabel">Welcome back!</h3>
                </div>
                <div class="inline-flex flex-column gap-2 mb-3">
                    <FloatLabel class="ip_float">
                        <InputText v-tooltip.top="'Enter your E-Mail'" id="ip_lg_email" name="ip_lg_email"
                            v-model="ip_lg_email" class="w-full ip_float bg-white-alpha-20" maxlength="35" autofocus />
                        <label for="ip_lg_email">E-Mail</label>
                    </FloatLabel>
                </div>
                <div class="inline-flex flex-column gap-2 mb-1">
                    <FloatLabel class="ip_float">
                        <InputText v-tooltip.top="'Enter your password'" id="ip_lg_password" name="ip_lg_password"
                            v-model="ip_lg_password" class="w-full ip_float bg-white-alpha-20" maxlength="35" />
                        <label for="ip_lg_password">Password</label>
                    </FloatLabel>
                </div>
                <div class="flex-modal align-items-center gap-3">
                    <Button label="Cancel" @click="closeCallback" text
                        class="p-3 w-full text-primary-50 border-1 border-white-alpha-30 hover:bg-white-alpha-10"
                        outlined></Button>
                    <Button label="Login" @click="closeCallback(); login();" text
                        class="p-3 w-full text-primary-50 border-1 border-white-alpha-30 hover:bg-white-alpha-10"
                        outlined></Button>
                </div>
                <div style="text-align: center; margin-top: 1rem;">
                    <p class="p-terms">Don't have an account?</p>
                    <Button label="Register" @click="login_visible = false; register_visible = true;" text class="text-primary-50"></Button>
                </div>
            </div>
        </template>
    </Dialog>
</template>

<script>
import { registerAccount, loginAccount } from '~/communication/accounts';


export default {
    methods: {
        
    },
    data() { return {} },
    mounted() { },
    setup() {
        const router = useRouter()
        const toast = useToast()
        const register_visible = ref(false)

        const ip_userName = ref(null);
        const ip_mail = ref(null);
        const ip_password = ref(null);

        const ip_type = ref(null);
        const checkedTerms = ref(false);

        const login_visible = ref(false);
        const ip_lg_email = ref(null);
        const ip_lg_password = ref(null);
        

        async function register() {
            let userName = ip_userName.value;
            let mail = ip_mail.value;
            let password = ip_password.value;

            if (!userName){
                toast.add({ severity: 'error', summary: 'No username provided', detail: 'Please provide a username', life: 3000 })
                return;
            }

            if (!mail){
                toast.add({ severity: 'error', summary: 'No e-mail provided', detail: 'Please provide an e-mail address', life: 3000 })
                return;
            }

            if (!password){
                toast.add({ severity: 'error', summary: 'No password provided', detail: 'Please provide a password', life: 3000 })
                return;
            }
            // console.log(ip_userName.value, ip_mail.value, ip_password.value)
            registerAccount(ip_mail.value, ip_userName.value, ip_password.value).then((res) => {
                if (res.status === 200){
                    toast.add({ severity: 'success', summary: 'Account created', detail: 'You can now login', life: 3000 })
                } else {
                    toast.add({ severity: 'error', summary: 'Account creation failed', detail: 'Please try again', life: 3000 })
                }
            })
            


            // router.push('/videochat')
        }

        async function login(){
            let email = ip_lg_email.value;
            let password = ip_lg_password.value;
            if (!email){
                toast.add({ severity: 'error', summary: 'No username provided', detail: 'Please provide a username', life: 3000 })
                return;
            }

            if (!password){
                toast.add({ severity: 'error', summary: 'No password provided', detail: 'Please provide a password', life: 3000 })
                return;
            }

            loginAccount(ip_lg_email.value, ip_lg_password.value).then((token) => {
                if (token) {
                    router.push('/videochat')
                    toast.add({ severity: 'success', summary: 'Login successful', detail: 'You are now logged in', life: 3000 })
                } else {
                    toast.add({ severity: 'error', summary: 'Login failed', detail: 'Please try again', life: 3000 })
                }
            })

            // router.push('/videochat')
        }

        return {register, login, register_visible, ip_userName, ip_mail, ip_password, ip_type, checkedTerms, login_visible, ip_lg_email, ip_lg_password}
    },
}
</script>