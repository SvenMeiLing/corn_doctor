<template>
    <n-space vertical :class="props.strClass"
             :wrap-item="false" :wrap="false"
    >
        <!--聊天框容器-->

        <n-scrollbar content-class="p-2" ref="containerRef">
            <transition-group enter-active-class="animate__animated animate__fadeIn animate__slower">
                <!--每条消息-->
                <n-card
                        bordered
                        embedded
                        title=""
                        class="w-fit even:ms-auto m-2"
                        size="small"
                        v-for="(item, index) in chatHistory"
                        :key="index"
                >
                    <template #header>
                        <n-avatar
                                class="me-auto"
                                size="medium"
                                color="none "
                                :src="item.avatar"
                        >
                            <template #default v-if="item.role==='user' && !item.avatar">
                                <n-icon class="text-black dark:text-white"
                                        :component="UserAvatarFilled"></n-icon>
                            </template>
                        </n-avatar>
                        <n-flex align="center" justify="center" :size="0">

                            <n-text tag="div">
                                {{ item.message }}
                            </n-text>
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
            ></n-input>
            <n-button class="h-full" @click="chatAI">发送</n-button>
        </n-flex>
    </n-space>
</template>

<script setup>
import {UserAvatarFilled} from '@vicons/carbon'
import {ref, onMounted, watch, nextTick} from "vue";
import {storeToRefs} from 'pinia'
import {useChatStore} from "@/stores/chatHistory.js"

import 'animate.css'

const props = defineProps({
    strClass: {
        // 用于title组件传递
        default: "mt-2 w-full h-5/6 rounded dark:bg-zinc-800",
        type: String
    }
})

const chatStore = useChatStore()
// 将 store 的 state 转换为 ref
const {localChatHistory} = storeToRefs(chatStore);


const chatHistory = ref([
    {
        id: 1,
        role: "spark",
        message: "您好, 我是基于讯飞星火的玉米医生,可为您解答有关农业相关的一切问题.",
        avatar: '/public/corn-logo.svg'
    },
    // {
    //     role: "user",
    //     message: "请问玉米叶斑病会自愈吗?",
    //     avatar: ""
    // },
    // {
    //     role: "spark",
    //     message: "玉米叶斑病是由真菌引起的病害，通常不会自愈。一旦玉米植株受到叶斑病的感染，如果不采取控制措施，病情往往会继续恶化，可能导致叶片凋萎、减少光合作用，影响玉米的生长和产量。",
    //     avatar: '/public/corn-logo.svg'
    // },
    // {
    //     role: "user",
    //     message: "好吧,谢谢",
    //     avatar: ""
    // }
])

const containerRef = ref(null);


const scrollBottom = () => {
    containerRef.value.scrollbarInstRef.containerRef.scrollTop = containerRef.value.scrollbarInstRef.containerRef.scrollHeight;
}
// 输入框双向绑定
const message = ref("")
const chatAI = async () => {
    // 发起请求前, 新增用户消息
    chatHistory.value.push({
        id: chatHistory.value.length + 1,
        role: "user",
        message: message.value,
        avatar: ""
    })

    let response = await fetch('http://127.0.0.1:8000/api/v1/ai-chat', {
        method: "POST",
        body: JSON.stringify({question: message.value}),
        headers: {
            'Content-Type': 'application/json' // 请求头，指定发送的数据类型为 JSON
            // 如果有其他请求头需要设置，可以在这里添加
        },
    });
    // 请求结束新增恢复信息
    chatHistory.value.push({
        id: chatHistory.value.length + 1,
        role: "spark",
        message: "",
        avatar: "/public/corn-logo.svg"
    })

    if (!response.ok) {
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

            chatStore.setLocalChatHistory(chatHistory.value)
            break;
        }

        const chunkText = textDecoder.decode(value);
        // 每次接收多少, 向消息中加入多少
        chatHistory.value[chatHistory.value.length - 1].message += chunkText

        // 滚动到指定内容
        scrollBottom();
    }
}


onMounted(() => {
    // 每次进入取出用户历史会话记录
    console.log(chatHistory.value)
    console.log(localChatHistory)
    if (chatHistory.value.length === 1 && localChatHistory.value.length > 1) {
        console.log("manxu")
        chatHistory.value = localChatHistory.value
    }
    watch(() => chatHistory.value.length, () => {
        console.log("chathistory变化了")
        nextTick(() => {
            console.log(containerRef.value.scrollbarInstRef)
            scrollBottom();
        });
    })
})

</script>

<style scoped>

</style>
