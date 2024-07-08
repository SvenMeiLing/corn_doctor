<template>
    <n-layout embedded class="p-[20px] h-full">
        <n-space vertical :wrap-item="false"
                 class="h-1/6"
        >
            <n-text tag="div" class="sm:text-xl md:text-2xl xl:text-3xl">
                本页面由
                <n-text tag="q" type="info">讯飞星火</n-text>
                赞助播出
            </n-text>
            <div class="aline mt-1"></div>
        </n-space>

        <n-space vertical class="mt-2 w-full h-5/6 rounded bg-zinc-100 dark:bg-zinc-800"
                 :wrap-item="false" :wrap="false"
        >

            <!--聊天框容器-->

            <n-scrollbar content-class="p-2">
                <!--每条消息-->
                <n-card
                        bordered
                        embedded
                        title=""
                        class="w-fit even:ms-auto m-2"
                        size="small"
                        v-for="item in chatHistory"
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


    </n-layout>

</template>

<script setup>
import {UserAvatarFilled} from '@vicons/carbon'
import {ref, reactive} from "vue";
import {getAIAnswer} from "@/apis/chatAI.js";
import axios from "axios";

const chatHistory = reactive([
    {
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

// 输入框双向绑定
const message = ref("")

const streamMsg = ref("")
const chatAI = async () => {
    // 发起请求前, 新增用户消息
    chatHistory.push({
        role: "user",
        message: message.value,
        avatar: ""
    })
    const res = await getAIAnswer({question: message.value})
    const reader = res.data.getReader();
    const decoder = new TextDecoder();
    while (true) {
        const {done, value} = await reader.read();
        console.log(value, ",,,,,,,____")
        if (done) break;

        const chunk = decoder.decode(value, {stream: true});
        streamMsg.value += chunk;
    }
    // 请求结束新增恢复信息
    // chatHistory.push({
    //     role: "spark",
    //     message: res,
    //     avatar: "/public/corn-logo.svg"
    // })
    // console.log(message.value)
    // console.log(res)
}
</script>

<style scoped>
.aline {
    width: 0;
    background-color: #3AA6B9;
    animation: expandWidth 2.5s ease-in-out infinite forwards;
    transition: all 2s ease;
}

@keyframes expandWidth {
    0% {
        width: 0;
        border: 0.01rem solid cadetblue;
    }
    30% {
        width: 30%;
        border: 0.015rem dotted lightcoral;
    }
    50% {
        width: 50%;
        border: 0.0175rem solid lightcoral;
    }
    70% {
        width: 70%;
        border: 0.019rem dotted palevioletred;
    }
    100% {
        width: 100%;
        border: 0.02rem dotted palevioletred;
    }
}

</style>
