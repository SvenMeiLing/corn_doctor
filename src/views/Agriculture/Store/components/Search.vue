<template>

    <n-select
            v-model:value="selectedValue"
            filterable
            placeholder="请输入"
            :options="options"
            class="mb-2"
            :show="isFilter"
            @search="isFilter = !isFilter"
            size=""
    >
        <template #empty>1</template>
    </n-select>


</template>

<script setup>
import {ref} from "vue";

const isFilter = ref(false)
const selectedValue = ref(null)
const selectedValues = ref(null)


const options = [
    {
        label: "Drive My Car",
        value: "song1"
    },
    {
        label: "Norwegian Wood",
        value: "song2"
    },
    {
        label: "You Won't See",
        value: "song3"
    },
    {
        label: "Nowhere Man",
        value: "song4"
    },
    {
        label: "Think For Yourself",
        value: "song5"
    },
    {
        label: "The Word",
        value: "song6"
    },
    {
        label: "Michelle",
        value: "song7"
    },
    {
        label: "What goes on",
        value: "song8"
    },
    {
        label: "Girl",
        value: "song9"
    },
    {
        label: "I'm looking through you",
        value: "song10"
    },
    {
        label: "In My Life",
        value: "song11"
    },
    {
        label: "Wait",
        value: "song12"
    }
]

</script>
