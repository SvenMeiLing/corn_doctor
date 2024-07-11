<template>
    <n-space vertical :wrap-item="false" :wrap="false"
             class="h-1/6"
    >
        <n-flex align="center">
            <n-text tag="div" class="sm:text-xl md:text-2xl xl:text-3xl">
                本页面由
                <n-text tag="q" type="info">讯飞星火</n-text>
                赞助播出
            </n-text>
            <n-divider vertical class="dark:bg-zinc-500"/>
            <MessageGroup />
            <n-popover>
                <template #trigger>
                    <n-icon @click="activate" :component="ArrowAnnotation" class="ms-auto cursor-pointer"
                            size="30"></n-icon>
                </template>
                <n-text>放大</n-text>
            </n-popover>
            <n-drawer
                    class="h-full"
                    v-model:show="activeRef"
                    :placement="placementRef"
                    to=".n-config-provider"
            >
                <n-drawer-content closable :native-scrollbar="false"
                                  class="h-full"
                                  body-content-class="h-full"
                >
                    <Chat :str-class="'h-full rounded dark:bg-zinc-800'"/>
                    <template #header>
                        <n-flex align="center" class="w-full">
                            <n-text>玉米医生@AI智能助理</n-text>
                        </n-flex>
                    </template>
                </n-drawer-content>

            </n-drawer>


        </n-flex>

        <div class="aline mt-1"></div>

    </n-space>
</template>

<script setup>
import {ArrowAnnotation} from "@vicons/carbon";
import {ref} from "vue";
import Chat from "@/views/Agriculture/AIChat/components/Chat.vue";
import MessageGroup from "@/views/Agriculture/AIChat/components/MessageGroup.vue";

const activeRef = ref(false)
const placementRef = ref("bottom")
const activate = () => {
    activeRef.value = true;
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
