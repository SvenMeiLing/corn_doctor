<template>
    <n-layout
            class="p-[20px] relative"
    >
        <div class="flex items-center gap-2">
            <!--标题-->
            <n-text class="text-2xl">
                农户社区
            </n-text>
            <n-button class="text-sm" size="tiny" type="info">
                疑难杂症 | 发帖提问
            </n-button>
        </div>


        <!--主体-->
        <n-layout
                content-class="gap-1 flex-nowrap"
                has-sider
        >
            <!--遇见一个bug， 布局总是自动换行， 加了has-sider就好了-->

            <!--帖子滚动容器-->
            <n-layout
                    :native-scrollbar="false"
                    class="w-3/5 sm:w-auto"
                    content-class="pe-3"
            >
                <!--帖子组-->
                <div class="lg:flex flex-nowrap gap-1">
                    <!--帖子-->
                    <n-card title="请问家里的玉米地这种病害该打什么药?"
                            header-class="p-1 text-base"
                            content-class="p-1"
                            class="lg:w-fit mb-1"
                    >
                        <template #cover>
                            <!--帖子图像-->
                            <div class="flex gap-2">
                                <n-image
                                        class="w-20"
                                        src="/src/assets/corn_category/blight.jpg"/>
                                <n-image
                                        class="w-20"
                                        src="/src/assets/corn_category/bs.jpg"/>
                            </div>
                        </template>

                        <!--帖子内容-->
                        <template #default>
                            <n-ellipsis>
                                最近突然发现家里的玉米地
                            </n-ellipsis>
                        </template>

                        <!--功能项-->
                        <template #action>
                            <!--点赞和评论-->
                            <div class="flex flex-nowrap items-center gap-4 text-sm">
                                <!--点赞-->
                                <div class="flex flex-nowrap items-center">
                                    <n-icon
                                            :component="Heart"
                                            v-if="liked"
                                            class="pointer"
                                            @click="clickLike"
                                    ></n-icon>
                                    <n-icon :component="HeartOutline" v-else
                                            @click="clickLike"
                                    ></n-icon>
                                    <n-text class="whitespace-nowrap">点赞</n-text>
                                </div>

                                <!--评论-->
                                <div class="flex flex-nowrap items-center">
                                    <n-icon :component="ChatFilled"></n-icon>
                                    <n-text class="whitespace-nowrap">评论</n-text>
                                </div>

                                <!--发贴事件-->
                                <div class="ms-auto">
                                    <n-text depth="3" class="text-xs whitespace-nowrap">{{ genDateTime() }}</n-text>
                                </div>
                            </div>
                        </template>
                    </n-card>

                    <n-card title="请问各位家里玉米地都用什么种子"
                            header-class="p-1 text-base"
                            content-class="p-1"
                            class="lg:w-fit mb-1"
                    >
                        <template #cover>
                            <!--帖子图像-->
                            <div class="flex gap-2">
                                <n-image
                                        class="w-20"
                                        src="/src/assets/corn_category/blight.jpg"/>
                                <n-image
                                        class="w-20"
                                        src="/src/assets/corn_category/bs.jpg"/>
                            </div>
                        </template>

                        <!--帖子内容-->
                        <template #default>
                            <n-ellipsis line-clamp="1" expand-trigger="click" :tooltip="false">
                                之前家里一直用的郑单958, 感觉抗病效果一般经常容易遭受被虫子啃
                            </n-ellipsis>
                        </template>

                        <!--功能项-->
                        <template #action>
                            <!--点赞和评论 -->
                            <div class="flex items-center gap-4 text-sm">
                                <!--点赞-->
                                <div class="flex items-center">
                                    <n-icon
                                            :component="Heart"
                                            v-if="liked"
                                            class="pointer"
                                            @click="clickLike"
                                    ></n-icon>
                                    <n-icon :component="HeartOutline" v-else
                                            @click="clickLike"
                                    ></n-icon>
                                    <n-text class="whitespace-nowrap">点赞</n-text>
                                </div>

                                <!--评论-->
                                <div class="flex items-center">
                                    <n-icon :component="ChatFilled"></n-icon>
                                    <n-text class="whitespace-nowrap">评论</n-text>
                                </div>

                                <!--发贴事件-->
                                <div class="ms-auto">
                                    <n-text depth="3" class="text-xs whitespace-nowrap">{{ genDateTime() }}</n-text>
                                </div>
                            </div>
                        </template>
                    </n-card>
                    <n-card title="请问各位家里玉米地都用什么种子"
                            header-class="p-1 text-base"
                            content-class="p-1"
                            class="lg:w-fit mb-1"
                    >
                        <template #cover>
                            <!--帖子图像-->
                            <div class="flex gap-2">
                                <n-image
                                        class="w-20"
                                        src="/src/assets/corn_category/blight.jpg"/>
                                <n-image
                                        class="w-20"
                                        src="/src/assets/corn_category/bs.jpg"/>
                            </div>
                        </template>

                        <!--帖子内容-->
                        <template #default>
                            <n-ellipsis line-clamp="1" expand-trigger="click" :tooltip="false">
                                之前家里一直用的郑单958, 感觉抗病效果一般经常容易遭受被虫子啃
                            </n-ellipsis>
                        </template>

                        <!--功能项-->
                        <template #action>
                            <!--点赞和评论 -->
                            <div class="flex items-center gap-4 text-sm">
                                <!--点赞-->
                                <div class="flex items-center">
                                    <n-icon
                                            :component="Heart"
                                            v-if="liked"
                                            class="pointer"
                                            @click="clickLike"
                                    ></n-icon>
                                    <n-icon :component="HeartOutline" v-else
                                            @click="clickLike"
                                    ></n-icon>
                                    <n-text class="whitespace-nowrap">点赞</n-text>
                                </div>

                                <!--评论-->
                                <div class="flex items-center">
                                    <n-icon :component="ChatFilled"></n-icon>
                                    <n-text class="whitespace-nowrap">评论</n-text>
                                </div>

                                <!--发贴事件-->
                                <div class="ms-auto">
                                    <n-text depth="3" class="text-xs whitespace-nowrap">{{ genDateTime() }}</n-text>
                                </div>
                            </div>
                        </template>
                    </n-card>
                </div>
            </n-layout>

            <!--aside侧边区域-->
            <aside class="gap-1 flex flex-col w-2/5 w-fit sm:w-fit h-fit">
                <!--热榜-->
                <n-list hoverable clickable class="w-full ms-auto">
                    <n-list-item>
                        <n-thing title="热门帖子" content-style="margin-top: 10px;">
                            <template #description>
                                <n-space size="small" style="margin-top: 4px" vertical>
                                    <n-tag :bordered="false" type="error" size="small">
                                        1.吡虫啉对植物的伤害
                                    </n-tag>
                                    <n-tag :bordered="false" size="small">
                                        2.华农101种子upup
                                    </n-tag>
                                    <n-tag :bordered="false" size="small">
                                        3.华农101种子upup
                                    </n-tag>
                                    <n-tag :bordered="false" size="small">
                                        4.先玉305销量再创佳绩upup
                                    </n-tag>
                                </n-space>
                            </template>
                        </n-thing>
                    </n-list-item>
                </n-list>

                <!--频道-->
                <n-list hoverable clickable class="w-full t ms-auto">
                    <n-list-item class="w-full">
                        <n-thing title="推荐分类" content-style="margin-top: 10px;">
                            <template #description>
                                <n-space size="small" style="margin-top: 4px">
                                   <n-text tag="ins">玉米</n-text>
                                   <n-text tag="ins">草莓</n-text>
                                   <n-text tag="ins">小麦</n-text>
                                   <n-text tag="ins">水稻</n-text>
                                   <n-text tag="ins">山药</n-text>
                                   <n-text tag="ins">葡萄</n-text>
                                   <n-text tag="ins">葡萄</n-text>
                                </n-space>
                            </template>
                        </n-thing>
                    </n-list-item>
                </n-list>

            </aside>


        </n-layout>
    </n-layout>

</template>

<script setup>
import {Heart, HeartOutline} from '@vicons/ionicons5'
import {ChatFilled} from '@vicons/material'
import {ref} from 'vue'
import {genDateTime} from "@/utils/genDateTime.js";

const liked = ref(false)

const clickLike = () => {
    liked.value = !liked.value
}
</script>

<style scoped>
:deep(.n-card__action) {
    /*card-action union 评论点赞*/
    padding: 10px;
}
</style>
