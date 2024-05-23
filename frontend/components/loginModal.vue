<style scoped></style>
<template>
    <Button label="Getting Started" icon="pi pi-user" outlined @click="login_visible = true" />
    <Dialog
            v-model:visible="login_visible"
            modal
            :pt="{
                root: 'border-none',
                mask: {
                    style: 'backdrop-filter: blur(2px)'
                }
            }"
        >
            <template #container="{ closeCallback }">
                <div class="flex-column px-5 py-5 gap-4" style="border-radius: 12px; background-color: var(--main-modal-bg); width: 320px;">
                    <div class="gap-2 mb-pi" style="justify-content: center; display: flex;">
                        <div class="iconBox" style="display: inline-flex;">
                            <img src="/img/logo_spintalk.png" style="width: 60px;"/>
                        </div>
                    </div>
                    <div class="inline-flex flex-column gap-2 mb-4" style="text-align: center;">
                        <h3 class="modal-title" id="createLobbyModalLabel">Start your Journey</h3>
                    </div>
                    <div class="inline-flex flex-column gap-2 mb-3">
                        <FloatLabel class="ip_float">
                            <InputText id="ip_username" name="ip_userName" v-model="ip_userName"
                                class="w-full ip_float bg-white-alpha-20" maxlength="20" />
                            <label for="ip_userName">Username</label>
                        </FloatLabel>
                    </div>
                    <div class="inline-flex flex-column gap-2 mb-3">
                        <FloatLabel class="ip_float">
                            <InputText id="ip_mail" name="ip_mail" v-model="ip_mail"
                                class="w-full ip_float bg-white-alpha-20" maxlength="20" />
                            <label for="ip_mail">E-Mail</label>
                        </FloatLabel>
                    </div>
                    <div class="flex-terms flex-column gap-2 mb-3">
                        <p class="p-terms">Acc. Terms & Cond.</p><InputSwitch v-model="checkedTerms"/>
                    </div>
                    <div class="flex-modal align-items-center gap-3">
                        <Button label="Cancel" @click="closeCallback" text class="p-3 w-full text-primary-50 border-1 border-white-alpha-30 hover:bg-white-alpha-10" outlined></Button>
                        <Button label="Start" @click="closeCallback" text class="p-3 w-full text-primary-50 border-1 border-white-alpha-30 hover:bg-white-alpha-10" outlined></Button>
                    </div>
                </div>
            </template>
        </Dialog>
</template>
<script setup>
const login_visible = ref(false)
const ip_userName = ref(null);
const ip_mail = ref(null);
const checkedTerms = ref(false);
</script>