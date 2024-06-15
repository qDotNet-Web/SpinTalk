<template>
    <div class="main-app">
        <h1 class="center">Accounts</h1>
        <InputText type="text" v-model="searchRef" placeholder="Search" class="mb-2" />

        <DataTable :value="filteredAccounts" :paginator="true" :rows="10" :rowsPerPageOptions="[5,10,20]" :emptyMessage="emptyMessage">
            <Column field="id" header="ID" sortable></Column>
            <Column field="username" header="Username" sortable></Column>
            <Column field="email" header="Email" sortable></Column>
            <Column field="role" header="Role" sortable></Column>
            <Column field="status" header="Status" sortable></Column>
            <Column field="created_at" header="Created At" sortable></Column>
            <Column field="last_updated" header="Updated At" sortable></Column>
            <Column field="last_login" header="Last Login" sortable></Column>
            <Column field="last_ip" header="Last IP" sortable></Column>
            <Column field="actions" header="Actions">    
              <template #body="slotProps">
                  <Button icon="pi pi-cog" @click="openDialog(slotProps.data)"></Button>
              </template>
            </Column>
        </DataTable>

        <Dialog v-model:visible="dialogVisible" maximizable modal header="Edit Profile" :style="{ width: '25rem' }">
          <template #header>
              <div class="inline-flex align-items-center justify-content-center gap-2" style="align-items: center;">
                  <Avatar :image="getUserAvatar(selectedAccount.id)" shape="circle" style="vertical-align: middle; margin-right: 0.5rem;" @error="handleImageError" />
                  <span class="font-bold white-space-nowrap">User Settings</span>
              </div>
          </template>

          <div class="flex-break mb-3">
            <label for="status" class="mb-1">Status</label>
            <div v-if="selectedAccount.status == 'active'">
              <Badge value="Active" severity="success" />
            </div>
            <div v-if="selectedAccount.status == 'banned'">
              <Badge value="Banned" severity="danger" />
            </div>
          </div>
          <div class="flex-break mb-3">
            <label for="email" class="mb-1">E-Mail</label>
            <InputText id="email" v-model="email" :value="selectedAccount.email" />
          </div>
          <div class="flex-break mb-3">
            <label for="username" class="mb-1">Username</label>
            <InputText id="username" v-model="username" :value="selectedAccount.username" />
          </div>
          <div class="flex-break mb-3">
            <label for="role" class="mb-1">Role</label>
            <Dropdown v-model="selectedRole" :options="roles" optionLabel="name" :placeholder="selectedAccount.role" />
          </div>
          <!-- actions (timeban, ban, unban) -->
          <h2 class="center">Actions</h2>
          <div class="flex-break mb-3 center">
            <Button label="Reset Password" text severity="success" icon="pi pi-refresh" @click="requireConfirmation($event)" />
            <div v-if="selectedAccount.status=='banned'">
              <Button label="Unban" text severity="success" icon="pi pi-unlock" />
            </div>
            <div v-if="selectedAccount.status=='active'">
              <Button label="Ban" text severity="danger" icon="pi pi-ban"  />
            </div>
            <Button label="Delete Account" text severity="danger" icon="pi pi-trash" />
          </div>
          <template #footer>
              <Button label="Cancel" text severity="secondary" @click="dialogVisible = false" autofocus />
              <Button label="Save" outlined severity="success" @click="dialogVisible = false" autofocus />
          </template>
      </Dialog>

    </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'acp'
})


import InputText from 'primevue/inputtext';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Dialog from 'primevue/dialog';
import { ref, computed, watchEffect } from 'vue'
import { useRoute } from 'vue-router';

const searchRef = ref('');



const accounts = ref([
{ id: 1, username: 'admin', email: ' [email protected]', role: 'admin', status: 'active', created_at: '2021-10-01', last_updated: '2021-10-01', last_login: '2021-10-01', last_ip: '192.168.1.1' },
  { id: 2, username: 'user', email: ' [email protected]', role: 'user', status: 'banned', created_at: '2021-10-01', last_updated: '2021-10-01', last_login: '2021-10-01', last_ip: '192.168.1.2' },
  { id: 3, username: 'moderator', email: ' [email protected]', role: 'moderator', status: 'active', created_at: '2021-10-01', last_updated: '2021-10-01', last_login: '2021-10-01', last_ip: '192.168.1.3' },
  { id: 4, username: 'guest', email: ' [email protected]', role: 'guest', status: 'active', created_at: '2021-10-01', last_updated: '2021-10-01', last_login: '2021-10-01', last_ip: '192.168.1.4' },
  { id: 5, username: 'test', email: ' [email protected]', role: 'user', status: 'active', created_at: '2021-10-01', last_updated: '2021-10-01', last_login: '2021-10-01', last_ip: '192.168.1.5' },
  { id: 6, username: 'test2', email: ' [email protected]', role: 'user', status: 'active', created_at: '2021-10-01', last_updated: '2021-10-01', last_login: '2021-10-01', last_ip: '192.168.1.6' },
  { id: 7, username: 'test3', email: ' [email protected]', role: 'user', status: 'active', created_at: '2021-10-01', last_updated: '2021-10-01', last_login: '2021-10-01', last_ip: '192.168.1.7' },
  { id: 8, username: 'test4', email: ' [email protected]', role: 'user', status: 'active', created_at: '2021-10-01', last_updated: '2021-10-01', last_login: '2021-10-01', last_ip: '192.168.1.8' },
  { id: 9, username: 'test5', email: ' [email protected]', role: 'user', status: 'active', created_at: '2021-10-01', last_updated: '2021-10-01', last_login: '2021-10-01', last_ip: '192.168.1.9' },
  { id: 10, username: 'test6', email: ' [email protected]', role: 'user', status: 'active', created_at: '2021-10-01', last_updated: '2021-10-01', last_login: '2021-10-01', last_ip: '192.168.1.10' },

])

const selectedAccount = ref(null);

const dialogVisible = ref(false);
const openDialog = (account: any) => {
  selectedAccount.value = account; // Update the ref, not the computed property
  dialogVisible.value = true;
};
let selectedRole = ref(null);
let filteredAccounts = computed(() => {
  // filter accounts by username or id or email
  return accounts.value.filter((account) => {
    let searchValue = searchRef.value.toLowerCase();
    let searchParts = searchValue.split(':');

    if (searchParts[0] === 'id' && account.id.toString() === searchParts[1]) {
      return true;
    }

    if (((searchParts[0] === 'username') || searchParts[0] === 'name') && account.username.toLowerCase() === searchParts[1]) {
      return true;
    }

    if (searchParts[0] === 'email' && account.email.toLowerCase() === searchParts[1]) {
      return true;
    }

    return account.username.toLowerCase().includes(searchValue) ||
      account.id.toString().includes(searchValue) ||
      account.email.toLowerCase().includes(searchValue);
  });
});

const route = useRoute();
watchEffect(() => {
  if (route.query.id) {
    searchRef.value = "id:"+route.query.id;
  } else if(route.query.username) {
    searchRef.value = "name:"+route.query.username;
  } else if(route.query.email) {
    searchRef.value = "email:"+route.query.email;
  }
});


function getUserAvatar(id: number) {
  return '/img/avatars/' + id + '.png';
}

function handleImageError(event: any) {
  event.target.src = '/img/testavatar.png';
}
const emptyMessage = 'No accounts found.';
const roles = ref([
  { name: 'admin', value: 'admin' },
  { name: 'moderator', value: 'moderator' },
  { name: 'user', value: 'user' }
])

</script>