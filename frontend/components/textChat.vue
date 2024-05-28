<template>
    <Card style="width: 100%" class="mb-3">
        <template #content>
            <div class="iconBox mb-3" style="display: inline-flex;">
                <i class="pi pi-comments text-5xl is-size-50 is-primary-color"></i>
            </div>
            <div class="flex-row overflow-y-auto mb-2" style="display: inline-flex">
                <div class="flex-row main-bg-color">
                    <div class="w-full" v-for="(chat, i) in chats" :key="i" :class="{
                        'justify-center': chat.username === 'Admin',
                        'justify-start': chat.username !== route.query.username,
                        'justify-end': chat.username === route.query.username,
                    }">
                        <div class="mb-3 rounded" :class="{
                            'bg-chat-sender': chat.username !== route.query.username,
                            'bg-chat-receiver': chat.username === route.query.username,
                            'bg-chat-admin': chat.username === 'Admin',
                        }">

                        </div>

                    </div>
                </div>

            </div>
        </template>
        <template #footer>
            <div class="flex-row mb-3">
                <InputGroup>
                    <InputText placeholder="Type your message.." />
                    <Button label="Send" outlined />
                </InputGroup>
            </div>
        </template>
    </Card>
</template>
<script setup lang="ts">
const route = useRoute();

interface Chat {
    username: string;
    text: string;
    time: string;
    room?: string;
}
type User = {
    id: string;
    username: string;
    room: string;
};
const message = ref('');
const chats = ref<Chat[]>([
    {
        username: 'John Doe',
        room: 'room1',
        text: 'Hello, how are you?',
        time: '10:44 PM',
    },
    {
        username: 'Jane Doe',
        room: 'room1',
        text: 'I am good, thanks!',
        time: '10:45 PM',
    }
]);
const users = ref<User[]>([
    {
        id: '1',
        username: 'John Doe',
        room: 'room1',
    },
    {
        id: '2',
        username: 'Jane Doe',
        room: 'room1',
    },
    {
        id: '3',
        username: 'Admin',
        room: 'room1',
    }
]);


</script>