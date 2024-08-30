<template>
    <n-layout-header bordered class="w-full h-14 md:h-24 lg:h-14 p-2">
        <n-space class="h-full w-full" :wrap="false" :wrap-item="false">

            <n-space :size="0"
                     class="w-full"
                     align="center"
                     :wrap-item="false" :wrap="false">
                <!--当屏幕尺寸小于sm时出现菜单按钮-->
                <n-button class="lg:hidden p-1"
                          :bordered="true"
                          @click="activate('left')"
                >
                    <n-icon :component="Menu" :size="30"></n-icon>
                </n-button>

                <!--logo+标题-->
                <n-icon :component="CornLogo" :size="40" class="text-3xl ms-auto sm:ms-0"></n-icon>
                <n-text class="font-thin text-lg md:text-xl text-[#E9C46A]">
                    智慧农业
                </n-text>
                <n-icon :component="X" size="15"></n-icon>
                <!--通过margin来保持双向居中-->
                <n-text type="success" class="font-thin text-lg md:text-xl">
                    玉米医生
                </n-text>

                <n-flex class="ms-auto w-1/4" justify="center" align="center">
                    <!--切换主题按钮-->
                    <n-button class="" circle @click="changeTheme(!isDarkTheme)">
                        <n-icon :component="theme.icon"></n-icon>
                    </n-button>
                    <!--签名-->
                    <n-text class="ms-auto">{{ userProfile.userinfo.signature }}</n-text>
                    <n-popover placement="bottom" trigger="click" class="p-0  w-72">
                        <template #trigger>
                            <!--头像区域-->
                            <n-avatar
                                    size="small"
                                    :src="userProfile.userinfo.avatar"
                                    class="flex items-center justify-center"
                            >
                                <!--图像加载失败时显示-->
                                <template #fallback>
                                    <n-icon :component="FaceWink" class="text-yellow-400 text-2xl"></n-icon>
                                </template>
                            </n-avatar>
                        </template>
                        <n-card title="用户信息"
                                class="bg-gray-900 dark:bg-zinc-900"
                        >
                            <template #default>
                                <n-text tag="b" type="info" class="mr-1 text-base">Hi</n-text>
                                <n-text class="text-lg">{{ userProfile.userinfo.username }}</n-text>
                                <n-divider/>
                                <n-statistic label="您拥有" tabular-nums>
                                    <n-number-animation ref="numberAnimationInstRef"
                                                        :from="0"
                                                        :to="userProfile.userinfo.credit"
                                                        precision="2"
                                    />
                                    <template #suffix>
                                        个积分
                                    </template>
                                    <template #prefix>$</template>
                                </n-statistic>
                            </template>
                            <template #footer>
                                <n-a :href="'#'" @click="logout">
                                    注销
                                </n-a>
                            </template>
                        </n-card>
                    </n-popover>


                </n-flex>

            </n-space>

        </n-space>

        <n-drawer
                to="#dark"
                v-model:show="activeRef"
                :placement="placementRef"
                resizable
                class="w-1/2"
        >
            <n-drawer-content
                    title="菜单选项"
                    body-content-class="p-1"
                    :native-scrollbar="false">
                <HomeMenu @drawer-show="handleDrawerShow"/>
            </n-drawer-content>
        </n-drawer>

    </n-layout-header>

</template>

<script setup>
import {ref} from 'vue'
import {useDesignSettingStore} from "@/stores/designSetting.js";
import {useUserProfile} from '@/stores/userProfile.js'
import {storeToRefs} from "pinia";


import CornLogo from '@/components/CornLogo.vue'
import X from '@/components/X.vue'
import {Menu, FaceWink} from '@vicons/carbon'
import HomeMenu from "@/views/Home/components/HomeMenu.vue";

const themeStore = useDesignSettingStore()
const userProfile = useUserProfile()
const {theme, isDarkTheme} = storeToRefs(themeStore)
const {changeTheme} = themeStore

const activeRef = ref(false);
const placementRef = ref("right");
const activate = (place) => {
    activeRef.value = true;
    placementRef.value = place;
};
const handleDrawerShow = (show) => {
    // 接收子组件(菜单组件)的菜单切换回调, 如若切换则自动关闭drawer组件
    activeRef.value = show
}

const logout = () => {
    // 注销

}
</script>

<style scoped>

</style>
