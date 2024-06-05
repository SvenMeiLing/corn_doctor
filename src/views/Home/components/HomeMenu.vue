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
import {useRoute} from 'vue-router'
import {computed, onMounted} from "vue";
import {
    BookOutline as BookIcon,
    PersonOutline as PersonIcon,
    WineOutline as WineIcon,
    HomeOutline as HomeIcon,
    EyeOutline as RecognitionIcon
} from "@vicons/ionicons5";
import {useUserProfile} from "@/stores/userProfile.js";

const route = useRoute()
const message = useMessage()
const userProfile = useUserProfile()
// 每次重载页面时, 优先使用上一次会话中的路由
const activeKey = ref(userProfile.profile.lastRoute)

// 读图标
function renderIcon(icon) {
    return () => h(NIcon, null, {default: () => h(icon)});
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
                to: '/recognition',
            },
            "Recognition"
        ),
        key: "Recognition",
        icon: renderIcon(RecognitionIcon)
    },
    {
        label: "1973年的弹珠玩具",
        key: "pinball-1973",
        icon: renderIcon(BookIcon),
        disabled: true,
        children: [
            {
                label: "鼠",
                key: "rat"
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
        label: "舞，舞，舞",
        key: "dance-dance-dance",
        icon: renderIcon(BookIcon),
        children: [
            {
                type: "group",
                label: "人物",
                key: "people",
                children: [
                    {
                        // label: "叙事者",
                        label: () => h(
                            RouterLink,
                            {
                                to: {path: `/page3/child1`},

                            }, {
                                default: () => "child1"
                            }
                        ),
                        key: "narrator",
                        icon: renderIcon(PersonIcon)
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
