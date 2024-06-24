<template>
    <router-link :to="to" v-slot="{ navigate, href }" custom>
        <n-a :href="href" @click="navigate" :class="[
        'no-underline',
        'hover:bg-slate-800',
        'rounded',className,'text-zinc-300'
        ]">
            <slot/>
        </n-a>
    </router-link>
</template>

<script setup>
import {computed} from 'vue';

// 使用 defineProps 声明 props
const props = defineProps({
    to: {
        type: [String, Object],
        required: true
    },
    className: {
        type: [String, Array, Object],
        default: ''
    }
});

</script>

<style scoped>

</style>
