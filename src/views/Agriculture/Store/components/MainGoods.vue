<template>
  <!-- 第二部分 -->
    <n-flex vertical class="h-min w-full md:w-1/2 xl:w-1/3">
        <n-card size="small" content-class="p-1 flex flex-wrap">
            <template #header>
                <n-text type="info" tag="div" class="rounded">{{ props.slogan }}</n-text>
                <n-text>环保型农药,活动期间</n-text>
                <n-text type="error">7折</n-text>
            </template>
            <n-card
                    class="h-30 w-1/2"
                    content-class="pb-0"
                    v-for="item in props.showGoods">
                <n-image
                        :src="item.img_src"
                        object-fit="contain"
                        width="100%"
                ></n-image>
                <template #footer>
                    <n-ellipsis :line-clamp="1">
                        <n-text tag="div">{{ item.name }}</n-text>
                    </n-ellipsis>
                    <n-text tag="div" class="text-sm" depth="3">{{item.dliver}}</n-text>
                    <n-text tag="div">
                        <n-text class="text-sm">￥</n-text>
                        <n-text class="text-xl" type="error">{{item.price}}</n-text>
                    </n-text>

                    <n-text class="p-1 rounded-lg text-sm bg-zinc-100 dark:bg-zinc-800">
                        {{item.shopName}} 进店>
                    </n-text>
                </template>
            </n-card>
        </n-card>
    </n-flex>
</template>

<script setup>
const props = defineProps({
    showGoods: {
        default: [],
        type: Array
    },
    slogan: {
        type: String
    }
})
</script>

<style scoped>

</style>
