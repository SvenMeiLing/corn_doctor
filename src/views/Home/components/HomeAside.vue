<template>

    <n-layout-sider
            :class="{'collapsed': collapsed}"
            bordered
            collapse-mode="width"
            :collapsed-width="64"
            :width="240"
            :collapsed="collapsed"
            show-trigger="bar"
            @collapse="collapsed = true"
            @expand="collapsed = false"
            content-style="padding:7px"
    >

        <n-message-provider>
            <n-scrollbar style="max-height: 500px" trigger="hover">
                <HomeMenu></HomeMenu>
            </n-scrollbar>
        </n-message-provider>
    </n-layout-sider>
</template>

<script setup>
import HomeMenu from "@/views/Home/components/HomeMenu.vue";
import {ref, watch, onMounted} from 'vue'
import {useUserProfile} from '@/stores/userProfile.js'

const userProfile = useUserProfile()
// 直接使用默认设置false, 如果用户变动则使用用户设定值
const collapsed = ref(userProfile.profile.collapsed)
watch(collapsed, (newValue) => {
    // 当用户切换菜单收缩时, 在会话中保存设置
    userProfile.setUserProfile('collapsed', newValue)
    // 也会添加一个类名
    console.log(collapsed.value)
})
onMounted(() => {
    // collapsed.value = userProfile.profile.collapsed
})
</script>

<style scoped>
* {
    transition: .5s ease;
}
</style>
