<template>
    <Line :data="chartData" :options="options" />
</template>

<script setup lang="ts">
import { computed } from "vue"
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
} from "chart.js";
import { Line } from "vue-chartjs";

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
);

const props = defineProps({
    priceSnapshots: Array
});

const chartData = computed(() => ({
    labels: props.priceSnapshots.map(s => s.time),
    datasets: [{
        label: "Price",
        data: props.priceSnapshots.map(s => parseFloat(s.price)),
        borderColor: "#16a34a",
        tension: 0.1
    }]
}));

const options = {
    responsive: true,
    maintainAspectRatio: false
};
</script>
