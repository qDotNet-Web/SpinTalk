<template>
    <div class="main-app">
        <Card style="width: 100%" class="mt-3 mb-3">
            <template #content>
                <spectateLobby></spectateLobby>
            </template>
        </Card>

        <textChat></textChat>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
// get room id from /
const route = useRoute();
const router = useRouter();
const roomId = ref(route.params.id);
if (!roomId.value) {
    router.push('/acp/rooms');
}
console.log(roomId.value);
</script>