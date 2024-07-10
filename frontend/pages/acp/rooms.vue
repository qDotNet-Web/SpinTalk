<template>
    <div class="main-app">
        <h1>Rooms</h1>
        <InputText type="text" v-model="searchRef" placeholder="Search" class="mb-2" />

        <DataTable :value="filteredRooms" :paginator="true" :rows="5" :rowsPerPageOptions="[5,10,20]" :emptyMessage="emptyMessage">
            <Column field="id" header="Room ID" sortable></Column>
            <Column field="user_one_id" header="User One ID"></Column>
            <Column field="user_one" header="User One"></Column>
            <Column field="user_two_id" header="User Two ID"></Column>
            <Column field="user_two" header="User Two"></Column>
            <Column field="actions" header="Actions">    
              <template #body="slotProps">
                  <Button icon="pi pi-eye" @click="viewRoom(slotProps.data)" style='margin-right: 0.2rem;'></Button>
                  <Button icon="pi pi-stop" @click="endConversation(slotProps.data)"></Button>
              </template>
            </Column>
        </DataTable>
    </div>
</template>

<script setup>
import { useToast } from 'primevue/usetoast';

import { ref, computed } from 'vue';
import {useRouter, useRoute} from 'vue-router';

const router = useRouter();
const toast = useToast();
definePageMeta({
  layout: 'acp'
})

const rooms = ref([
    { id: 1, user_one_id: 1, user_one: 'User One', user_two_id: 2, user_two: 'User Two' },
    { id: 2, user_one_id: 2, user_one: 'User Two', user_two_id: 3, user_two: 'User Three' },
    { id: 3, user_one_id: 3, user_one: 'User Three', user_two_id: 4, user_two: 'User Four' },
    { id: 4, user_one_id: 4, user_one: 'User Four', user_two_id: 5, user_two: 'User Five' },
    { id: 5, user_one_id: 5, user_one: 'User Five', user_two_id: 6, user_two: 'User Six' },
    { id: 6, user_one_id: 6, user_one: 'User Six', user_two_id: 7, user_two: 'User Seven' },
    { id: 7, user_one_id: 7, user_one: 'User Seven', user_two_id: 8, user_two: 'User Eight' },
    { id: 8, user_one_id: 8, user_one: 'User Eight', user_two_id: 9, user_two: 'User Nine' },
    { id: 9, user_one_id: 9, user_one: 'User Nine', user_two_id: 10, user_two: 'User Ten' },
    { id: 10, user_one_id: 10, user_one: 'User Ten', user_two_id: 11, user_two: 'User Eleven' },
])

const searchRef = ref('')

let filteredRooms = computed(() => {
    // filter by search and by id: and user_one: and user_two:
    return rooms.value.filter(room => {
        return room.id.toString().includes(searchRef.value) || room.user_one_id.toString().includes(searchRef.value) || room.user_one.includes(searchRef.value) || room.user_two_id.toString().includes(searchRef.value) || room.user_two.includes(searchRef.value)
    })
})


function viewRoom(room) {
    // spectate room on a new page
    router.push(`/acp/spectate/${room.id}`)
}


function endConversation(room) {
    toast.add({ severity: 'success', summary: 'Conversation Ended', detail: 'Conversation has been ended', life: 3000 });
    rooms.value = rooms.value.filter(r => r.id !== room.id)
}
</script>