<template>
    <n-menu :options="menuOptions"
            @update:value="handleUpdateValue"
            v-model:value="activeKey"
    />
</template>

<script setup>
import {watch, ref, h} from "vue";
import {NIcon, useMessage} from "naive-ui";
import {RouterLink} from "vue-router";

import {
    BookOutline as BookIcon,
    WineOutline as WineIcon,
    HomeOutline as HomeIcon,
    EyeOutline as RecognitionIcon,
} from "@vicons/ionicons5";
import {
    StoreMallDirectoryTwotone as StoreIcon,
    BubbleChartTwotone as Chart
} from '@vicons/material'
import {Template, FlowStreamReference} from '@vicons/carbon'
import {useUserProfile} from "@/stores/userProfile.js";
import drone from '@/components/drone.vue'
import NounBook from '@/components/NounBook.vue'

const message = useMessage()
const userProfile = useUserProfile()
// 每次重载页面时, 优先使用上一次会话中的路由
const activeKey = ref(userProfile.profile.lastRoute)

// 读图标
function renderIcon(icon, props) {
    return () => h(NIcon, props, {default: () => h(icon)});
}

const menuOptions = [
    {
        label: () => h(
            RouterLink,
            {
                to: {
                    path: '/',
                }
            },
            {default: () => "回家"}  // 弹出消息
        ),
        key: "home",
        icon: renderIcon(HomeIcon), // 图标
    },
    {
        key: "divider-1",
        type: "divider",
        props: {
            style: {
                marginLeft: "32px"
            }
        }
    },
    {
        label: () => h(
            RouterLink,
            {
                to: '/recognition'
            },
            "图像识别"
        ),
        key: "Recognition",
        icon: renderIcon(RecognitionIcon)
    },

    {
        label: "无人机平台",
        key: "pinball-1973",
        icon: renderIcon(drone, {size: 30}),
        disabled: false,
        children: [
            {
                label: "监控",
                key: "rat",
                icon: renderIcon(BookIcon)
            }
        ]
    },
    {
        label: "寻羊冒险记",
        key: "a-wild-sheep-chase",
        icon: renderIcon(BookIcon),
        disabled: true
    },
    {
        label: "服务平台",
        key: "agriculture",
        icon: renderIcon(Template),
        children: [
            {
                type: "group",
                label: "Platform",
                key: "people",
                children: [
                    {
                        // label: "叙事者",
                        label: () => h(
                            RouterLink,
                            {
                                to: {path: `/agriculture/disease`},

                            }, {
                                default: () => "病害百科"
                            }
                        ),
                        key: "disease",
                        icon: renderIcon(NounBook)
                    },
                    {
                        label: () => h(
                            RouterLink,
                            {
                                to: {path: `/agriculture/store`},

                            }, {
                                default: () => "农业商城"
                            }
                        ),
                        key: "store",
                        icon: renderIcon(StoreIcon)
                    },
                    {
                        label: () => h(
                            RouterLink,
                            {
                                to: {path: `/agriculture/ai-chat`},

                            }, {
                                default: () => "智能助理"
                            }
                        ),
                        key: "aiChat",
                        icon: renderIcon(Chart),
                    },
                ]
            },

        ]
    },
    {
        label: () => h(
            RouterLink,
            {
                to: '/flow-recognition'
            },
            "流式识别"
        ),
        key: "flow-recognition",
        icon: renderIcon(FlowStreamReference)
    }
];
const emit = defineEmits(["drawerShow"])

const handleUpdateValue = (key, item) => {
    // 菜单路由切换时触发, 收纳抽屉
    emit("drawerShow", false)
    // message.info("[onUpdate:value]: " + JSON.stringify(key));
    // message.info("[onUpdate:value]: " + JSON.stringify(item));
}


watch(activeKey, (newRoute) => {
    // 当路由发生改变就去记录一次
    userProfile.setUserProfile("lastRoute", newRoute)
})

</script>

<style scoped>

</style>
