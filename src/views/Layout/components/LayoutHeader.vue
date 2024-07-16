<template>
    <n-layout-header bordered class="w-full h-16 md:h-24 lg:h-14 p-2">
        <n-space class="h-full w-full" :wrap="false" :wrap-item="false">

            <n-space :size="0"
                     class="justify-center w-full "
                     align="center"
                     :wrap-item="false" :wrap="false">
                <!--当屏幕尺寸小于sm时出现菜单按钮-->
                <n-button class="lg:hidden p-1"
                          :bordered="false"
                          @click="activate('left')"
                >
                    <n-icon :component="Menu" :size="30"></n-icon>
                </n-button>

                <!--logo+标题-->
                <n-icon :component="CornLogo" :size="40" class="ms-auto md:ms-0"></n-icon>
                <n-text class="font-thin text-xl text-[#E9C46A]">
                    智慧农业
                </n-text>
                <n-icon :component="X" size="15"></n-icon>
                <n-text type="success" class="font-thin text-xl">
                    玉米医生
                </n-text>

                <!--切换主题按钮-->
                <n-button class="ms-auto" circle @click="changeTheme(!isDarkTheme)">
                    <n-icon :component="theme.icon"></n-icon>
                </n-button>
            </n-space>

        </n-space>

        <n-drawer
                v-model:show="activeRef"
                :placement="placementRef"
                resizable
                class="w-60"
        >
            <n-drawer-content
                    title="菜单选项"
                    :native-scrollbar="false">
                <HomeMenu/>
            </n-drawer-content>
        </n-drawer>

    </n-layout-header>

</template>

<script setup>
import {ref} from 'vue'
import {useDesignSettingStore} from "@/stores/designSetting.js";
import {storeToRefs} from "pinia";

import CornLogo from '@/components/CornLogo.vue'
import X from '@/components/X.vue'
import {Menu} from '@vicons/carbon'
import HomeMenu from "@/views/Home/components/HomeMenu.vue";

const themeStore = useDesignSettingStore()
const {theme, isDarkTheme} = storeToRefs(themeStore)
const {changeTheme} = themeStore

const activeRef = ref(false);
const placementRef = ref("right");
const activate = (place) => {
    activeRef.value = true;
    placementRef.value = place;
};
</script>

<style scoped>

</style>
