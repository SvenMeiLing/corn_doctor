<template>
    <n-layout embedded class="p-[20px] h-full">
        <Child :list="list"></Child>
        <button @click="list.push(1)">加</button>
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
import {ref, onMounted, toRefs} from 'vue'
import localforage from 'localforage'
import {v4 as uuid4} from "uuid"
import Child from "@/views/Page5/Child.vue";

const themeStore = useDesignSettingStore()
const {theme} = storeToRefs(themeStore)
const list = ref([2])

const markDownText = ref(
    "# 玉米日记 \n\n  " +
    "## 今天我们去了玉米地 \n\n  " +
    "### 路上发现了一个玉米医生 \n\n " +
    "这是玉米地🌽" +
    "\n\n![风景图](https://images.pexels.com/photos/533738/pexels-photo-533738.jpeg?auto=compress&cs=tinysrgb&w=600)\n" +
    "> 啊!我爱玉米\n" +
    "> > 啊!玉米爱我\n" +
    "> > > 啊!玉米\n" +
    "> > > >啊!我\n" +
    "> > > > >啊!"
)
onMounted(async () => {
// todo: 先去库中找配置项, 例如最大存储几组消息, 每组可以存储多少条消息, 每条消息对应一个uuid唯一值和时间, 最后的会话(数组最后一项)
//  如果存在历史记录就取出记录 config: {}
    const msgGroup = [
        {
            uuid: uuid4(),
            data: [
                {
                    "dateTime": "2024/7/9 10:56:35",  // 消息时间
                    "text": "我国现有多少玉米品种" // 用户消息内容
                },
                {
                    "dateTime": "2024/7/9 10:59:35",  // 消息时间
                    "text": "大概10多种" // 用户消息内容
                },
            ],
            lastSession: false
        },
        {
            uuid: uuid4(),
            data: [
                {
                    "dateTime": "2024/7/10 10:56:35",  // 消息时间
                    "text": "玉米病虫害大类" // 用户消息内容
                },
                {
                    "dateTime": "2024/7/9 10:59:35",  // 消息时间
                    "text": "有十几种大类" // 用户消息内容
                },
            ], lastSession: true
        },
        {
            uuid: uuid4(),
            data: [
                {
                    "dateTime": "2024/7/11 10:56:35",  // 消息时间
                    "text": "抗病玉米种子中价格实惠的是哪种?" // 用户消息内容
                },
                {
                    "dateTime": "2024/7/9 10:59:35",  // 消息时间
                    "text": "京玉非常良好" // 用户消息内容
                },
            ], lastSession: false
        },
        {
            uuid: uuid4(),
            data: [
                {
                    "dateTime": "2024/7/14 10:56:35",  // 消息时间
                    "text": "玉米叶枯病的治疗手段" // 用户消息内容
                },
                {
                    "dateTime": "2024/7/9 10:59:35",  // 消息时间
                    "text": "多喷药,多使用玉米医生系统" // 用户消息内容
                },
            ], lastSession: false
        },
    ]
    console.log(msgGroup.value)
    const myIndexedDB = localforage.createInstance({name: 'cornIndexedDB',})
    await myIndexedDB.setItem("names", ['xxx', "xzz", 'asss'])

    await myIndexedDB.setItem("chatHistory", msgGroup)
    const value = await myIndexedDB.getItem('names');
    value.push("zzy")
    await myIndexedDB.setItem("names", value)

    console.log(value);
})
</script>
<style scoped>

</style>
