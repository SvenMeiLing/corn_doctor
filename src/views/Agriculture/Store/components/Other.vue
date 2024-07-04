<template>
  <!-- 第三部分 -->
    <n-flex vertical class=" w-full md:w-1/2 xl:w-1/3">
        <n-card size="small">
            <template #header>
                新品速推
            </template>
            <template #default>
                <n-carousel show-arrow class="w-72 h-72">
                    <img
                            v-for="item in props.newProduct"
                            class="w-full h-full object-contain"
                            :src="item.img_src"
                    >

                </n-carousel>
            </template>
        </n-card>
    </n-flex>
</template>

<script setup>
import DJI from '@/components/DJI.vue'
import iFlytek from '@/components/iFlytek.vue'

const props = defineProps({
    newProduct: {
        default: [],
        type: Array
    }
})
</script>

<style scoped>
.carousel-img {
    width: auto;
    height: 300px;
}
</style>
