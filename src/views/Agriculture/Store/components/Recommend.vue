<template>
  <!--第一部分-->
    <n-flex vertical class="h-min w-full md:w-1/2 xl:w-1/3">

        <!--标题-->
        <n-h6 prefix="bar" type="error" class="m-0">
            <n-icon class="text-red-400" :component="HotelClassTwotone"></n-icon>
            <n-text type="error">推荐商品</n-text>
        </n-h6>
        <!--商品展示区域-->
        <div class="
        w-full h-full
        collapsed:grid-cols-3
        grid grid-cols-2

        gap-x-1 gap-y-2
        dark:bg-zinc-800
        rounded p-2">

            <!--渲染每个商品-->
            <div class="goods-recommend
                    hover:bg-zinc-400 bg-zinc-200
                    cursor-pointer
                    rounded h-min" v-for="item in props.recommendList"
            >
                <div class="card
                        dark:bg-zinc-900
                        hover:dark:bg-zinc-700
                        p-1 h-full flex flex-col items-center">
                    <img :src="item.img_src" alt="" class="w-full h-[100px] object-contain">
                </div>
                <div class="bg-zinc-300 dark:bg-gray-700 p-2 w-full flex items-center">
                    <n-text class="text-sm" type="default">{{ item.name }}</n-text>
                    <n-icon class="ml-auto text-red-400" :component="RMB"></n-icon>
                    <n-text class="text-base" type="error">{{ item.price }}</n-text>
                </div>
            </div>
        </div>


    </n-flex>
</template>

<script setup>

import {HotelClassTwotone} from "@vicons/material";
import RMB from "@/components/RMB.vue";

const props = defineProps({
    recommendList: {
        default: [],
        type: Array
    }
})
</script>

<style scoped>

</style>
