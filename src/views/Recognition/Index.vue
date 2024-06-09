<template>

    <n-layout embedded style="border: 1px solid skyblue" class="p-[20px]">
        <!--        标题与模态框合体-->
        <UploadView></UploadView>

        <n-space class="mt-2" vertical style="border: 1px solid red">
            <n-data-table class="shadow-lg rounded-md" :columns="createColumns" :data="data"/>
        </n-space>


    </n-layout>
</template>
<script setup>
import UploadView from "@/views/Recognition/components/UploadView.vue";
import {computed, ref} from "vue";


const createColumns = computed(() => {
    return [
        {
            title: '#',
            key: 'num'
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
const data = ref([])
onMounted(() => {
    data.value.push(
        {
            num: 1,
            name: '...',
            consuming: "...",
            desc: "..."
        }
    )
    // 打印
    console.log('000')
})

</script>
<style scoped>

</style>
<style>
#nprogress .bar {
    background-color: palevioletred;
}
</style>
