<template>
    <n-layout embedded class="p-[20px] h-full"
              content-class="flex items-center justify-center">
        <n-result status="404" title="404 资源不存在" description="生活总归带点荒谬">
            <template #footer>
                <n-button @click="router.replace('/')">回到首页</n-button>
            </template>
        </n-result>
    </n-layout>
</template>
<script setup>
import {useRouter} from "vue-router";

const router = useRouter()

</script>
