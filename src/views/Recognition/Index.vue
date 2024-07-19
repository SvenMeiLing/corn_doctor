<template>

    <n-layout embedded class="p-[20px] h-full">
        <!--标题与模态框合体-->
        <UploadView></UploadView>
        <!--这个组件需要缓存,切换路由时数据依然是最后一次的-->

        <TableView></TableView>


    </n-layout>
</template>
<script setup>
import UploadView from "@/views/Recognition/components/UploadView.vue";
import TableView from "@/views/Recognition/components/TableView.vue";
import {onActivated} from 'vue'

onActivated(() => {
    console.log('我是父组件')
})

</script>
<style scoped>

</style>
<style>
#nprogress .bar {
    background-color: palevioletred;
}
</style>
