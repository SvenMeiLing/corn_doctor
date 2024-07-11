<template>
    <MdPreview
            :class="props.classList"
            :showCodeRowNumber="true"
            :modelValue="markDownText"
            :theme="theme.title"
    />

</template>

<script setup>
import {MdPreview} from 'md-editor-v3'
import 'md-editor-v3/lib/style.css'
import {storeToRefs} from "pinia";
import {useDesignSettingStore} from "@/stores/designSetting.js";

const props = defineProps({
    // markdown格式字符
    markDownText: {
        type: String
    },
    // 由于某些原因(未知因素), 抽屉组件感应不到dark, 所以需要给出class以便在使用抽屉组件时客制化marked组件的样式
    classList: {
        default: "dark:bg-zinc-800 rounded",
        type: String
    }
})

const themeStore = useDesignSettingStore()
const {theme} = storeToRefs(themeStore)

const markDownText = ref(props.markDownText)

</script>
<style scoped>
</style>
