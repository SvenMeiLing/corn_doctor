<template>
  <!-- 第三部分 -->
    <n-flex vertical class=" w-full md:w-1/2 xl:w-1/3">
        <n-card title="限时促销" size="small">
            使用期间,优质种子
            <n-text type="error">7折</n-text>
            促销
        </n-card>
        <n-card>
            <n-text tag="div">
                <n-icon :component="DJI" :size="30"></n-icon>
                大疆无人机 x 玉米医生
            </n-text>
            <n-divider/>
            <n-text tag="div">
                <n-icon :component="iFlytek" :size="60"></n-icon>
                科大讯飞 x 玉米医生
            </n-text>
            <n-divider/>
        </n-card>
    </n-flex>
</template>

<script setup>
import DJI from '@/components/DJI.vue'
import iFlytek from '@/components/iFlytek.vue'
</script>

<style scoped>

</style>
