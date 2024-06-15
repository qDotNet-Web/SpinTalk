<template>
    <div class="main-app">
        <h1>Bans</h1>
        <!-- <DataTable :value="bans" :paginator="true" :rows="10" :rowsPerPageOptions="[5,10,20]" :emptyMessage="emptyMessage">
            <Column field="id" header="ID"></Column>
            <Column field="user_id" header="User ID"></Column>
            <Column field="username" header="Username"></Column>
            <Column field="reason" header="Reason"></Column>
            <Column field="expires_at" header="Expires At" sortable></Column>
            <Column field="created_at" header="Created At"></Column>
            <Column field="created_by" header="Created By" sortable></Column>
            <Column field="actions" header="Actions">
                <template #body="slotProps">
                    <Button icon="pi pi-pencil" @click="openDialog(slotProps.data)"></Button>
                </template>
            </Column>
        </DataTable> -->

        <h2>Coming soon...</h2>
    </div>
</template>

<script setup>
definePageMeta({
  layout: 'acp'
})
const emptyMessage = 'No bans found';
const bans = ref(
    [
        {
            id: 1,
            user_id: 1,
            username: 'test',
            reason: 'test',
            expires_at: '2021-01-01 00:00:00',
            created_at: '2021-01-01 00:00:00',
            created_by: 'test',
        },
        {
            id: 2,
            user_id: 2,
            username: 'test2',
            reason: 'test2',
            expires_at: '2021-01-01 00:00:00',
            created_at: '2021-01-01 00:00:00',
            created_by: 'test2',
        }
    ]
)
</script>