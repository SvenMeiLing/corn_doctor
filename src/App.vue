<template class="first">
    <n-config-provider
            :theme="theme.name" :id="theme.title"
            >
        <RouterView/>
    </n-config-provider>
</template>
<script setup>
import {onMounted} from 'vue'
import {storeToRefs} from "pinia";
import {useDesignSettingStore} from "@/stores/designSetting.js";
import {darkTheme} from 'naive-ui'


const themeStore = useDesignSettingStore()
const {theme} = storeToRefs(themeStore)
const {changeTheme} = themeStore
onMounted(() => {
    // 监听storage中主题变化, 动态切换
    window.addEventListener('storage', event => {
        console.log(event)
        if (event.key === 'theme') {
            const newTheme = JSON.parse(event.newValue)
            changeTheme(newTheme.isDarkTheme)
        }
    })
})
</script>
<style>

.n-config-provider {
    height: 100%;
    width: 100%;
}

.n-layout-scroll-container {
    /*这是n-layout组件的内容(content)样式*/
    display: flex;
    height: 100%;
    width: 100%;
    flex-direction: column;
}
</style>
