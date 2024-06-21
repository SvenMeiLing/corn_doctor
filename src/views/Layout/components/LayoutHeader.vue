<template>
    <n-layout-header style="padding: 0 20px;" bordered>
        <n-space justify="space-between" align="center" style="height: 100%;">
            <n-space :size="0" justify="center" align="center">
                <n-image src="/src/assets/images/corn.png" height="30" preview-disabled></n-image>

                <n-text type="success" align-text="center" style="font-size: 150%;font-weight: 300;">
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

const themeStore = useDesignSettingStore()
const {theme, isDarkTheme} = storeToRefs(themeStore)
const {changeTheme} = themeStore
</script>

<style scoped>

</style>
