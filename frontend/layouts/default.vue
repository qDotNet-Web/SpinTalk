<template>
    <div>
        <AppHeader />
        <Menubar :model="items">
            <template #start>
                <div class="flex align-items-center gap-2">
                    <img src="/img/logo_trans.png" style="width: 44px;"/>
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
                <div class="flex align-items-center gap-2" style="display: flex;">
                    <InputText placeholder="Search" type="text" class="w-8rem sm:w-auto" />
                    <Avatar image="/img/testavatar.png" shape="circle" />
                </div>
            </template>
        </Menubar>
        <slot />
        <AppFooter />
    </div>
</template>

<script setup>
const router = useRouter()
const items = ref([
    {
        label: 'Home',
        icon: 'pi pi-home',
        command: () => {
            router.push('/');
        }
    },
    {
        label: 'Account',
        icon: 'pi pi-user'
    },
    {
        label: 'Video',
        icon: 'pi pi-video',
    },
    {
        label: 'Chat',
        icon: 'pi pi-comments',
    },
    {
        label: 'About',
        icon: 'pi pi-info-circle',
        command: () => {
            router.push('/about');
        }
    }
]);

</script>