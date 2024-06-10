<template>

    <n-layout embedded style="border: 1px solid skyblue" class="p-[20px]">
        <!--标题与模态框合体-->
        <UploadView ref="zzy"></UploadView>
        <!--这个组件需要缓存,切换路由时数据依然是最后一次的-->
        <keep-alive>
            <component :is="TableView" :key="$route.path"></component>
        </keep-alive>


    </n-layout>
</template>
<script setup>
import UploadView from "@/views/Recognition/components/UploadView.vue";
import TableView from "@/views/Recognition/components/TableView.vue";

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
