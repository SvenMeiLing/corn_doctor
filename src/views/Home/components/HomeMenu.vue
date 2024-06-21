<template>
    <n-menu :options="menuOptions"
            @update:value="handleUpdateValue"
            v-model:value="activeKey"
    />
</template>

<script setup>
import {h} from "vue";
import {NIcon, useMessage} from "naive-ui";
import {RouterLink} from "vue-router";
import {onMounted} from "vue";
import {
    BookOutline as BookIcon,
    PersonOutline as PersonIcon,
    WineOutline as WineIcon,
    HomeOutline as HomeIcon,
    EyeOutline as RecognitionIcon
} from "@vicons/ionicons5";
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
        label: "农业知识",
        key: "agriculture",
        icon: renderIcon(BookIcon),
        children: [
            {
                type: "group",
                label: "Learn",
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
                        label: "羊男",
                        key: "sheep-man",
                        icon: renderIcon(PersonIcon)
                    }
                ]
            },
            {
                label: "饮品",
                key: "beverage",
                icon: renderIcon(WineIcon),
                children: [
                    {
                        label: "威士忌",
                        key: "whisky"
                    }
                ]
            },
            {
                label: "食物",
                key: "food",
                children: [
                    {
                        label: "三明治",
                        key: "sandwich"
                    }
                ]
            },
            {
                label: "过去增多，未来减少",
                key: "the-past-increases-the-future-recedes"
            }
        ]
    }
];
const handleUpdateValue = (key, item) => {
    message.info("[onUpdate:value]: " + JSON.stringify(key));
    message.info("[onUpdate:value]: " + JSON.stringify(item));
}


watch(activeKey, (newRoute) => {
    // 当路由发生改变就去记录一次
    userProfile.setUserProfile("lastRoute", newRoute)
})
onMounted(() => {

})
</script>

<style scoped>

</style>
