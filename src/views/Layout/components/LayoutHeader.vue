<template>
    <n-layout-header style="padding: 0 20px;" bordered>
        <n-space justify="space-between" align="center" style="height: 100%;">
            <n-space :size="0" justify="center" align="center" :wrap-item="false" :wrap="false">
                <!--                <n-image src="/src/assets/images/corn.png" height="30" preview-disabled></n-image>-->
                <n-icon :component="CornLogo" :size="40" class="text-yellow-600"></n-icon>
                <n-text class="font-thin text-xl">
                    智慧农业
                </n-text>
                <n-icon :component="X" size="15"></n-icon>
                <n-text type="success" class="font-thin text-xl">
                    玉米医生
                </n-text>
            </n-space>
            <n-space>
                <n-button circle @click="changeTheme(!isDarkTheme)">
                    <n-icon :component="theme.icon"></n-icon>
                </n-button>
            </n-space>


        </n-space>
    </n-layout-header>

</template>

<script setup>
import {useDesignSettingStore} from "@/stores/designSetting.js";
import {storeToRefs} from "pinia";

import CornLogo from '@/components/CornLogo.vue'
import X from '@/components/X.vue'

const themeStore = useDesignSettingStore()
const {theme, isDarkTheme} = storeToRefs(themeStore)
const {changeTheme} = themeStore
</script>

<style scoped>

</style>
