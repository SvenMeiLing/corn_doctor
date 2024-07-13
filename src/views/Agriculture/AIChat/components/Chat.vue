<template>
    <n-space vertical :class="props.strClass"
             :wrap-item="false" :wrap="false"
    >
        <!--聊天框容器-->
        <n-scrollbar content-class="p-2" ref="containerRef">
            <transition-group enter-active-class="animate__animated animate__fadeIn animate__slower">
                <!--系统消息-->
                <n-card
                        bordered
                        embedded
                        title=""
                        class="w-fit me-auto m-2"
                        size="small"
                >
                    <template #header>
                        <n-avatar
                                class="me-auto"
                                size="medium"
                                color="none "
                                src="/public/corn-logo.svg"
                        >
                        </n-avatar>
                        <n-flex align="center" justify="center" :size="0">
                            <Marked :mark-down-text="'🌽我是玉米医生智能AI客服,为您解答与农业相关的问题'"/>
                        </n-flex>
                    </template>
                </n-card>

                <!--每条消息-->
                <n-card
                        bordered
                        embedded
                        title=""
                        class="w-fit even:ms-auto m-2"
                        size="small"
                        v-for="(item, index) in chatHistory.data"
                        v-if="chatHistory"
                        :key="index"
                >
                    <template #header>
                        <n-avatar
                                class="me-auto"
                                size="medium"
                                color="none "
                                src="/public/corn-logo.svg"
                        >
                            <template #default v-if="index % 2 === 0">
                                <n-icon class="text-black dark:text-white"
                                        :component="UserAvatarFilled"></n-icon>
                            </template>
                        </n-avatar>
                        <n-flex align="center" justify="center" :size="0">
                            <Marked :mark-down-text="item.text"/>
                        </n-flex>
                    </template>
                </n-card>
            </transition-group>
        </n-scrollbar>
        <n-flex
                :wrap="false"
                align="center"
                class="p-1"
        >
            <n-input
                    placeholder="请输入你的问题:"
                    type="textarea"
                    :autosize="{
                            minRows: 1,
                            maxRows: 5
                         }"
                    v-model:value="message"
                    @keydown.enter="sendQuestion"
            ></n-input>
            <n-button class="h-full" @click="sendQuestion">发送</n-button>
        </n-flex>
    </n-space>
</template>

<script setup>
import {UserAvatarFilled} from '@vicons/carbon'
import {ref, onMounted, watch, nextTick, toRefs, toRaw} from "vue";
import {storeToRefs} from 'pinia'
import {useChatStore} from "@/stores/chatHistory.js"

import Marked from "@/views/Agriculture/AIChat/components/Marked.vue"
import 'animate.css'
import {genDateTime} from "@/utils/genDateTime.js";
import {chatAI} from "@/apis/chatAI.js";
import localforage from "localforage";

const chatStore = useChatStore()
// 将 store 的 state 转换为 ref
const {localChatHistory} = storeToRefs(chatStore);

const myIndexedDB = localforage.createInstance({name: 'cornIndexedDB',})
// const chatHistory = ref([
//     {
//         id: 1,
//         role: "spark",
//         message: "您好, 我是基于讯飞星火的玉米医生,可为您解答有关农业相关的一切问题.",
//         avatar: '/public/corn-logo.svg'
//     },
//     // {
//     //     role: "user",
//     //     message: "请问玉米叶斑病会自愈吗?",
//     //     avatar: ""
//     // },
//     // {
//     //     role: "spark",
//     //     message: "玉米叶斑病是由真菌引起的病害，通常不会自愈。一旦玉米植株受到叶斑病的感染，如果不采取控制措施，病情往往会继续恶化，可能导致叶片凋萎、减少光合作用，影响玉米的生长和产量。",
//     //     avatar: '/public/corn-logo.svg'
//     // },
//     // {
//     //     role: "user",
//     //     message: "好吧,谢谢",
//     //     avatar: ""
//     // }
// ])
const props = defineProps({
    strClass: {
        // 用于title组件传递
        default: "mt-2 w-full h-5/6 rounded dark:bg-zinc-800",
        type: String
    },
    chatHistory: {
        default: [
            {
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
        ],
        type: Array
    },
    list: {
        default: [],
        type: Array
    }
})

const {chatHistory} = toRefs(props)
const containerRef = ref(null);

const scrollBottom = () => {
    // 使其消息容器滚动到底部
    containerRef.value.scrollbarInstRef.containerRef.scrollTop = containerRef.value.scrollbarInstRef.containerRef.scrollHeight;
}
// 输入框双向绑定
const message = ref("")
// 封装发送消息的函数

const sendQuestion = async () => {
    // todo:发送消息时, 如果该消息组data为null, 则更改标题为此消息的text字段
    // 发起请求前, 向会话中新增用户提问消息
    chatHistory.value.data.push({
        dateTime: genDateTime(),
        text: message.value
    })
    // 用户发送消息后滚动到底部
    scrollBottom()

    // 发起请求, 获取流式响应对象
    let response = await chatAI(message.value)

    // 清空输入框值
    message.value = ""

    // 新增ai恢复, 在流式请求中逐渐更新text的值
    chatHistory.value.data.push({
        dateTime: genDateTime(),
        text: "",
    })

    if (!response.ok) {
        // 如果请求失败, 消息内容将变成提示信息
        chatHistory.value.data[chatHistory.value.data.length - 1].text = "网络错误, 请重新试试呢!🤣"
        throw new Error('Network response was not ok');
    }

    const reader = response.body.getReader();
    const textDecoder = new TextDecoder();
    let result = true;

    while (result) {
        const {done, value} = await reader.read();

        if (done) {
            // 流式接收结束
            result = false;
            // 使其再次规整消息到底部, 偶尔bug导致,最后结尾预防一下没有滚动到底部的情况
            scrollBottom()

            // 结束会话后, 持久化最新消息到客户端

            // 先获取原有消息组中的消息
            const oldMsgGroup = await myIndexedDB.getItem("chatHistory")
            const newMsgGroup = oldMsgGroup.map(group => {
                if (group.uuid === chatHistory.value.uuid) {
                    return toRaw(chatHistory.value)
                }
                return toRaw(group)
            })
            console.log(newMsgGroup, "<*******")
            await myIndexedDB.setItem("chatHistory", newMsgGroup)
            break;
        }

        const chunkText = textDecoder.decode(value);
        // 每次接收多少, 向消息中加入多少
        chatHistory.value.data[chatHistory.value.data.length - 1].text += chunkText

        // 滚动到指定内容
        scrollBottom();
    }
}


onMounted(() => {
    // 若用户有历史消息记录, 每次进入取出用户历史会话记录
    // if (chatHistory.value.length === 1 && localChatHistory.value.length > 1) {
    //     console.log("内存中存在历史消息记录")
    //     chatHistory.value = localChatHistory.value
    //     nextTick(() => {
    //         // 等待dom加载完毕, 把滚动条恢复到消息的底部
    //         scrollBottom();
    //     })
    // }
    // 监听消息变化, 实时触发滚动到底部的函数
    watch(() => chatHistory.value.length, () => {
        // 每当消息变化则触发更新滚动条使其滑动到底部
        nextTick(() => {
            console.log(containerRef.value.scrollbarInstRef)
            scrollBottom();
        });
    })
    // watch(chatHistory, (newVal) => {
    //     console.log(newVal)
    // })
})

</script>

<style scoped>

</style>
