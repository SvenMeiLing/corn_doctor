<template>
    <n-layout embedded class="p-[20px] h-full">

        <MdPreview
                class="dark:bg-zinc-900 rounded"
                :showCodeRowNumber="true"
                :modelValue="markDownText"
                :theme="theme.title"
        />

    </n-layout>
</template>

<script setup>
import {MdPreview} from 'md-editor-v3'
import 'md-editor-v3/lib/style.css'
import {storeToRefs} from "pinia";
import {useDesignSettingStore} from "@/stores/designSetting.js";

const themeStore = useDesignSettingStore()
const {theme} = storeToRefs(themeStore)

const markDownText = ref(
    "# 玉米日记 \n\n  " +
    "## 今天我们去了玉米地 \n\n  " +
    "### 路上发现了一个玉米医生 \n\n " +
    "这是玉米地🌽" +
    "\n\n![风景图](https://images.pexels.com/photos/533738/pexels-photo-533738.jpeg?auto=compress&cs=tinysrgb&w=600)\n" +
    "> 啊!我爱玉米\n" +
    "> > 啊!玉米爱我\n" +
    "> > > 啊!玉米\n" +
    "> > > >啊!我\n"
)
//初始化
// const markdownRender =
//     new MarkdownIt({
//         html: true,
//         linkify: true,
//         typographer: true,
//     }).use(markdownItImsize)
const renderMdText = (text) => {
    //生成html
    return markdownRender.render(text)
}

</script>
<style scoped>

</style>
