<template>
    <SpeedDial :model="items" direction="up" :style="{ right: '15px', bottom: '15px' }" />
</template>

<script setup>
    import { useToast } from 'primevue/usetoast';

    const toast = useToast();
    const router = useRouter();

    const items = ref([
        {
            label: 'Add User',
            icon: 'pi pi-user-plus',
            command: () => {
                toast.add({ severity: 'success', summary: 'Add User', detail: 'User Added' });
            }
        },
        {
            label: 'Report User',
            icon: 'pi pi-flag',
            command: () => {
                toast.add({ severity: 'warn', summary: 'Report User', detail: 'Report Sent' });
            }
        }
    ])
</script>