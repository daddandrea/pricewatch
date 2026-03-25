<script setup>
import PriceChart from "./components/PriceChart.vue"
import { ref, onMounted } from "vue";
import axios from "axios";

const coins = ref([]);
const form = ref({
    coin_id: "",
    name: "",
    threshold: "",
    tolerance: "",
    alert_above: false,
});

const selectedCoin = ref({
    coin_id: "",
    name: "",
});

const priceSnapshots = ref([]);

const error = ref(null);

onMounted(async () => {
    const response = await axios.get("/api/coins/");
    coins.value = response.data;
});

async function addCoin() {
    try {
        const response = await axios.post("/api/coins/", form.value);
        coins.value.push(response.data);
        form.value = {
            coin_id: "",
            name: "",
            threshold: "",
            tolerance: "",
            alert_above: false,
        };
        error.value = null;
    } catch (err) {
        error.value = err.response?.data?.detail || "Failed to add coin.";
    }
}

function selectCoin(coin) {
    selectedCoin.value = {
        coin_id: coin.coin_id,
        name: coin.name,
    };
}

async function fetchPriceSnapshot(coin_id) {
    const url = "/api/price_snapshots/?coin_id=" + coin_id;
    try {
        const response = await axios.get(url);
        priceSnapshots.value = response.data;

        error.value = null;
    } catch (err) {
        error.value = err.response?.data?.detail || "Failed to fetch price snapshot for selected coin";
    }
}
</script>

<template>
    <div class="container">
        <h1>PriceWatch</h1>

        <form class="coin-form" @submit.prevent="addCoin">
            <h2>Add Coin</h2>
            <input
                v-model="form.coin_id"
                placeholder="Coin ID (e.g. bitcoin)"
                required
            />
            <input
                v-model="form.name"
                placeholder="Name (e.g. Bitcoin)"
                required
            />
            <input
                v-model="form.threshold"
                type="number"
                step="0.01"
                placeholder="Threshold"
                required
            />
            <input
                v-model="form.tolerance"
                type="number"
                step="0.01"
                placeholder="Tolerance"
                required
            />
            <label>
                <input v-model="form.alert_above" type="checkbox" />
                Alert above threshold
            </label>
            <p v-if="error" class="error-message">{{ error }}</p>
            <button type="submit">Add</button>
        </form>

        <ul class="coin-list">
            <li
                v-for="coin in coins"
                :key="coin.coin_id"
                class="coin-item"
                @click="() => {
                    selectCoin(coin)
                    fetchPriceSnapshot(coin.coin_id)
                }"
            >
                <span class="coin_id">{{ coin.coin_id }}</span>
                <span class="name">{{ coin.name }}</span>
                <span class="last_price_snapshot">{{
                    coin.last_price_snapshot
                        ? coin.last_price_snapshot + "$"
                        : "N/A"
                }}</span>
            </li>
        </ul>

        <div v-if="priceSnapshots.length > 0" class="chart-container">
            <PriceChart :priceSnapshots="priceSnapshots" />
        </div>
    </div>
</template>

<style scoped>
.container {
    max-width: 480px;
    margin: 40px auto;
    font-family: sans-serif;
}

h1 {
    margin-bottom: 24px;
}

.coin-form {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-bottom: 32px;
    padding: 20px;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
}

.coin-form h2 {
    margin: 0 0 8px;
}

.coin-form input[type="text"],
.coin-form input[type="number"],
.coin-form input:not([type]) {
    padding: 8px 12px;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    font-size: 14px;
}

.coin-form label {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 14px;
}

.coin-form button {
    padding: 8px 16px;
    background: #16a34a;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 14px;
}

.coin-list {
    list-style: none;
    padding: 0;
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.coin-item {
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 16px;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
}

.coin_id {
    font-weight: bold;
    width: 48px;
}

.name {
    flex: 1;
    color: #555;
}

.last_price_snapshot {
    font-weight: 600;
    color: #16a34a;
    min-width: 80px;
    text-align: right;
}

.error-message {
    color: #dc2626;
    font-size: 14px;
    margin: 0;
}

.chart-container {
  height: 300px;
  margin-top: 32px;
}
</style>
