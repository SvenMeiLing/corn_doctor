<template>
    <n-space class="v-tb mt-2" vertical style="border: 1px solid red">
        <n-data-table class="shadow-lg rounded-md" :columns="createColumns" :data="data"/>
        <input type="text">
    </n-space>


</template>

<script setup>
import {onMounted, computed, ref, onUnmounted} from "vue";
import emitter from "@/utils/mitt.js";


const createColumns = computed(() => {
    return [
        {
            title: '#',
            key: 'id'
        },
        {
            title: '名称',
            key: 'name'
        },
        {
            title: '耗时/置信度',
            key: 'consuming'
        },
        {
            title: '描述',
            key: 'desc'
        }
    ]
})
const data = ref([{
    id: 1,
    name: '...',
    consuming: "...",
    desc: "..."
}])

onMounted(() => {
    emitter.on('recognitionData', (recognitionData) => {
        // 如果有数据传递才去渲染,没有则不渲染
        if (recognitionData) {
            console.log(recognitionData)
            data.value = recognitionData?.map((value, index) => {
                return {
                    id: index + 1,
                    ...value
                }
            })
        } else {
            console.log('没有数据了')
        }

    })
})
onActivated(() => {
    console.log('我是子组件')
})
// 移除
onUnmounted(() => {
    emitter.off('recognitionData', () => {
    })
})
</script>
