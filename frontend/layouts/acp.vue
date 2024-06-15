<style>
    #logo:hover {
        cursor: pointer;
    }
</style>

<template>
<div>
    <AppHeader />
    <Menubar :model="items">
        <template #start>
                <div class="flex align-items-center gap-2" style="display: flex; padding-right: .2rem;">
                    <img src="/img/logo_spintalk.png" id="logo" style="width: 40px;" @click="router.push('/')"/>
                </div>
        </template>
        <template #item="{ item, props, hasSubmenu, root }">
                <a v-ripple class="flex align-items-center" v-bind="props.action">
                    <span :class="item.icon" />
                    <span class="ml-2">{{ item.label }}</span>
                    <Badge v-if="item.badge" :class="{ 'ml-auto': !root, 'ml-2': root }" :value="item.badge" />
                    <span v-if="item.shortcut"
                        class="ml-auto border-1 surface-border border-round surface-100 text-xs p-1">{{ item.shortcut
                        }}</span>
                    <i v-if="hasSubmenu"
                        :class="['pi pi-angle-down', { 'pi-angle-down ml-2': root, 'pi-angle-right ml-auto': !root }]"></i>
                </a>
        </template>
        <template #end>
            <div class="flex align-items-center gap-2" style="display: flex; gap: 0.4rem">
                    <Avatar image='/img/testavatar.png' shape="circle" @click="" />
                </div>
        </template>
    </Menubar>
    <slot />
    <AppFooter />
</div>
    
</template>


<script setup>
    import { ref } from 'vue'
    import { useRouter } from 'vue-router'
    const router = useRouter();
        const items = ref([
            {
                label: 'Statistics',
                icon: 'pi pi-chart-bar',
                command: () => {
                    router.push('/acp')
                }
            },
            {
                label: 'Accounts',
                icon: 'pi pi-user',
                command: () => {
                    router.push("/acp/accounts")
                }
            },
            {
                label: 'Rooms',
                icon: 'pi pi-video',
                command: () => {
                    router.push("/acp/rooms")
                }
            },
            {
                label: 'Reports',
                icon: 'pi pi-flag',
                command: () => {
                    router.push("/acp/reports")
                }
            },
            {
                label: 'Bans',
                icon: 'pi pi-ban',
                command: () => {
                    router.push("/acp/bans")
                }
            },
            {
                label: 'Roles',
                icon: 'pi pi-users',
                command: () => {
                    router.push("/acp/roles")
                }
            },  
        ]);
</script>