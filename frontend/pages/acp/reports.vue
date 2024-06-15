<template>
    <div class="main-app">
        <h1>Reports</h1>
        <DataTable :value="filteredReports" :paginator="true" :rows="10" :rowsPerPageOptions="[5,10,20]" :emptyMessage="emptyMessage">
            <Column field="id" header="Report ID" sortable></Column>
            <Column field="reporter_id" header="Reporter ID"></Column>
            <Column field="reporter" header="Reporter"></Column>
            <Column field="reported_id" header="Reported ID"></Column>
            <Column field="reported" header="Reported"></Column>
            <Column field="reason" header="Reason" sortable></Column>
            <Column field="status" header="Status" sortable></Column>
            <Column field="created_at" header="Created At" sortable></Column>
            <Column field="actions" header="Actions">    
              <template #body="slotProps">
                  <Button icon="pi pi-pencil" @click="openDialog(slotProps.data)"></Button>
              </template>
            </Column>
        </DataTable>

        <Dialog v-model:visible="dialogVisible" maximizable modal header="" :style="{ width: '50rem' }">
          <template #header>
            <div class="inline-flex align-items-center justify-content-center gap-2" style="align-items: center;">
                <Avatar image="/img/testavatar.png" shape="circle" style="vertical-align: middle; margin-right: 0.5rem;" />
                <span class="font-bold white-space-nowrap" style="vertical-align: middle;">Report Info #{{ selectedReport.id }}</span>
            </div>
          </template>
            <div class="flex-break mb-3 center">
                <label for="reason" class="mb-1">Reason</label>
                <Badge :value="selectedReport.reason" severity="danger" />
            </div>
            <Divider />
            <div style="display: flex; justify-content: space-between;">
                <div class="left">
                    <label for="reported" class="mb-1">Reported User</label>
                    <nuxt-link class="custom-link mb-1" v-if="selectedReport.reported_id" :to="{name: 'acp-accounts', query: {id: selectedReport.reported_id}}"><Badge :value="selectedReport.reported" severity="danger" /></nuxt-link>
                </div>
                
                <div class="right">
                    <label for="reported" class="mb-1">Reported by</label>
                    <nuxt-link class="custom-link mb-1" v-if="selectedReport.reporter_id" :to="{name: 'acp-accounts', query: {id: selectedReport.reporter_id}}"><Badge :value="selectedReport.reporter" severity="success" /></nuxt-link>
                </div>
            </div>

            <div style="display: flex; justify-content: space-between;" class="mb-3">
                <img :src="`/img/reports/report_${selectedReport.id}/0.png`" alt="" class="report-preview" @error="handleImageError" />
                <img :src="`/img/reports/report_${selectedReport.id}/1.png`" alt="" class="report-preview" @error="handleImageError" />
            </div>
            
            <Divider />

            <label for="chatMessages" class="center mb-1">Messages</label>
            <div class="flex-break chatMessages">
                <div v-for="message in messages" :key="message.id" class="message">
                    <div v-if="message.user_id == selectedReport.reporter_id" class="message_a">
                        <div class="message-user right">{{ message.user }}</div>
                        <div class="message-text right">{{ message.message }}</div>
                        <div class="message-date right">{{ message.created_at }}</div>
                    </div>
                    <div v-else class="message_b">
                        <div class="message-user">{{ message.user }}</div>
                        <div class="message-text">{{ message.message }}</div>
                        <div class="message-date">{{ message.created_at }}</div>
                    </div>
                </div>
            </div>
            <Divider />

            <div style="display: flex; justify-content: space-between;">
                <Button label="Ban Reported User" text severity="danger" icon="pi pi-ban" />
                <Button label="Ban Reporting User" text severity="danger" icon="pi pi-ban" />
            </div>
          <template #footer>
              <Button label="Cancel" text severity="secondary" @click="dialogVisible = false" autofocus />
              <Button label="Archive" outlined severity="success" @click="dialogVisible = false" autofocus />
          </template>
      </Dialog>
    </div>
</template>

<script setup>
definePageMeta({
  layout: 'acp'
})
import { useRoute } from 'vue-router';

const emptyMessage = 'No reports found.';
let filteredReports = ref([
    { id: 1, reporter: 'User1', reporter_id: 1, reported: 'User2', reported_id: 2, reason: 'Spam', status: 'pending', created_at: '2021-10-01' },
    { id: 2, reporter: 'User2', reporter_id: 2, reported: 'User3', reported_id: 3, reason: 'Harassment', status: 'pending', created_at: '2021-10-02' },
    { id: 3, reporter: 'User3', reporter_id: 3, reported: 'User1', reported_id: 1, reason: 'Inappropriate Content', status: 'pending', created_at: '2021-10-03' },
    { id: 4, reporter: 'User4', reporter_id: 4, reported: 'User5', reported_id: 5, reason: 'Spam', status: 'pending', created_at: '2021-10-04' },
    { id: 5, reporter: 'User5', reporter_id: 5, reported: 'User6', reported_id: 6, reason: 'Harassment', status: 'pending', created_at: '2021-10-05' },
    { id: 6, reporter: 'User6', reporter_id: 6, reported: 'User4', reported_id: 4, reason: 'Inappropriate Content', status: 'pending', created_at: '2021-10-06' },
    { id: 7, reporter: 'User7', reporter_id: 7, reported: 'User8', reported_id: 8, reason: 'Spam', status: 'pending', created_at: '2021-10-07' },
    { id: 8, reporter: 'User8', reporter_id: 8, reported: 'User9', reported_id: 9, reason: 'Harassment', status: 'pending', created_at: '2021-10-08' },
    { id: 9, reporter: 'User9', reporter_id: 9, reported: 'User7', reported_id: 7, reason: 'Inappropriate Content', status: 'pending', created_at: '2021-10-09' },
    { id: 10, reporter: 'User10', reporter_id: 10, reported: 'User11', reported_id: 11, reason: 'Spam', status: 'pending', created_at: '2021-10-10' },
]);
let dialogVisible = ref(false);
let selectedReport = ref({});
let selectedReportIndex = ref(0);

let messages = ref([
    { id: 1, user_id: 1, message: 'Hello', created_at: '19:23:39' },
    { id: 2, user_id: 2, message: 'Hi', created_at: '19:23:40' },
    { id: 3, user_id: 1, message: 'How are you?', created_at: '19:23:41' },
    { id: 4, user_id: 2, message: 'I am fine', created_at: '19:23:42' },
    { id: 5, user_id: 1, message: 'Good to hear', created_at: '19:23:43' },
    { id: 6, user_id: 2, message: 'How about you?', created_at: '19:23:44' },
    { id: 7, user_id: 1, message: 'I am good too', created_at: '19:23:45' },
    { id: 8, user_id: 2, message: 'That is great', created_at: '19:23:46' },
    { id: 9, user_id: 1, message: 'Yes', created_at: '19:23:47' },
    { id: 10, user_id: 2, message: 'Bye', created_at: '19:23:48' },
    { id: 11, user_id: 1, message: 'Goodbye', created_at: '19:23:49' },
    { id: 12, user_id: 2, message: 'See you later', created_at: '19:23:50' },
    { id: 13, user_id: 1, message: 'Yes', created_at: '19:23:51' },
    { id: 14, user_id: 2, message: 'Bye', created_at: '19:23:52' },
    { id: 15, user_id: 1, message: 'Goodbye', created_at: '19:23:53' },
    { id: 16, user_id: 2, message: 'See you later', created_at: '19:23:54' },
    { id: 17, user_id: 1, message: 'Yes', created_at: '19:23:55' },

]);

function openDialog(report) {
    selectedReport.value = { ...report };
    selectedReportIndex.value = filteredReports.value.indexOf(report);
    dialogVisible.value = true;
}
function openReportById(id) {
    const report = filteredReports.value.find(report => report.id === id);
    if (report) {
        openDialog(report);
    }
}

function handleImageError(event) {
    event.target.src = 'https://www.sistemacoris.com/assets/images/no-image.png';
}

let route = useRoute()
if (route.query.id) {
    openReportById(parseInt(route.query.id));
}
</script>