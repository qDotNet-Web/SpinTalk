<template>
    <SpeedDial :model="items" :radius="120" type="quarter-circle" direction="up-left" :style="{ right: '10px', bottom: '15px' }" />
</template>

<script setup>

    const toast = useToast();
    const router = useRouter();

    const items = ref([
        {
            label: 'Add User',
            icon: 'pi pi-user-plus',
            command: () => {
                toast.add({ severity: 'info', summary: 'Add User', detail: 'User Added' })
            }
        },
        {
            label: 'Report User',
            icon: 'pi pi-flag',
            command: () => {
                toast.add({ severity: 'info', summary: 'Report User', detail: 'Report Sent' })
            }
        }
    ])
</script>