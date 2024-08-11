<template>
    <div class="main-app">
        <h1 class="center">Admin Control Panel</h1>
        <h2>Statistics</h2>
        <div class="chart-container">
            <!-- users & rooms -->
            <Chart :type="'line'" :data="chartData" :options="chartOptions" class="h-40rem w-50p"/>
            <!-- reports & bans -->
            <Chart :type="'line'" :data="chartData2" :options="chartOptions" class="h-40rem w-50p"/>            
        </div>
        <Nuxt />
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import Chart from 'primevue/chart';

import '~/assets/css/primevue.css'
import '~/assets/css/style.css'
definePageMeta({
  layout: 'acp'
})
const chartData = ref({
    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    datasets: [
        {
            label: 'Users',
            data: [65, 59, 80, 81, 56, 55, 40, 60, 55, 70, 75, 80],
            fill: true,
            borderColor: '#007be5',
            backgroundColor: 'rgba(0, 123, 229, 0.1)',
        },
        {
            label: 'Rooms',
            data: [28, 48, 40, 19, 86, 27, 90, 70, 55, 60, 65, 70],
            fill: true,
            borderColor: '#20d077',
            backgroundColor: 'rgba(32, 208, 119, 0.1)'
        },
    ]
});
const chartData2 = ref({
    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    datasets: [
        {
            label: 'Reports',
            data: [65, 59, 80, 81, 56, 55, 40, 60, 55, 70, 75, 80],
            fill: true,
            borderColor: 'orange',
            backgroundColor: 'rgba(255, 180, 0, 0.1)'
        },
        {
            label: 'Bans',
            data: [28, 48, 40, 19, 86, 27, 90, 70, 55, 60, 65, 70],
            fill: true,
            borderColor: 'red',
            backgroundColor: 'rgba(255, 0, 0, 0.1)'
        },
    ]
});
const chartOptions = ref({
    responsive: true,
    maintainAspectRatio: false,
});
</script>