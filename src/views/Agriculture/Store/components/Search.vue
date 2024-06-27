<template>

    <n-select
            v-model:value="selectedValue"
            filterable
            placeholder="搜索商品"
            :options="props.goodsList"
            class="mb-2 w-1/4"
            :show="isFilter"
            @input="isFilter = true"
            :show-arrow="true"
            clearable
    >
        <template #empty>
            <n-text class="text-sm">

            </n-text>
        </template>
    </n-select>


</template>

<script setup>
import {ref} from "vue";

const props = defineProps({
    goodsList: {
        default: [],
        type: Array
    }
})
const isFilter = ref(false)
const selectedValue = ref(null)
const selectedValues = ref(null)

onMounted(() => {
    window.addEventListener("click", () => {
        isFilter.value = false
    })
})
// todo: 点击选项后, 显示搜索到商品的页面
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
