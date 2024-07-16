<template>
    <n-layout-header bordered class="w-full h-16 md:h-24 lg:h-14 p-2">
        <n-space class="h-full w-full" :wrap="false" :wrap-item="false">
            <n-space :size="0"
                     class="justify-center w-full "
                     align="center"
                     :wrap-item="false" :wrap="false">

                <n-icon :component="CornLogo" :size="40"></n-icon>
                <n-text class="font-thin text-xl text-[#E9C46A]">
                    智慧农业
                </n-text>
                <n-icon :component="X" size="15"></n-icon>
                <n-text type="success" class="font-thin text-xl">
                    玉米医生
                </n-text>
                <n-button class="ms-auto" circle @click="changeTheme(!isDarkTheme)">
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
