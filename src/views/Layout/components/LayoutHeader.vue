<template>
    <n-layout-header bordered class="w-full h-14 md:h-14 lg:h-14 p-2">
        <n-space class="h-full w-full" :wrap="false" :wrap-item="false">

            <n-space :size="0"
                     class="w-full"
                     align="center"
                     :wrap-item="false" :wrap="false">
                <!--当屏幕尺寸小于sm时出现菜单按钮-->
                <n-button class="sm:block hidden p-1"
                          :bordered="true"
                          @click="activate('left')"
                >
                    <n-icon :component="Menu" :size="30"></n-icon>
                </n-button>

                <!--logo+标题-->
                <n-icon :component="CornLogo" :size="40" class="text-3xl ms-auto sm:ms-2"></n-icon>
                <n-text class="font-thin text-lg md:text-xl text-[#E9C46A]">
                    智慧农业
                </n-text>
                <n-icon :component="X" size="15"></n-icon>
                <!--通过margin来保持双向居中-->
                <n-text type="success" class="font-thin text-lg md:text-xl">
                    玉米医生
                </n-text>

                <n-flex class="ms-auto w-1/4 sm:flex w-auto" justify="center" align="center">
                    <!--头像区域-->
                    <n-popover placement="bottom-start" trigger="click" class="p-0  w-72">
                        <template #trigger>
                            <!--头像区域-->
                            <n-avatar
                                    size="medium"
                                    :src="userProfile.userinfo.avatar"
                                    class="bg-gray-200 dark:bg-zinc-700 flex items-center justify-center"
                            >
                                <!--图像加载失败时显示-->
                                <template #fallback>
                                    <n-icon :component="FaceWink" class="text-yellow-400 text-3xl"></n-icon>
                                </template>
                            </n-avatar>
                        </template>
                        <n-card title="用户信息">
                            <template #default>
                                <!--用户名称-->
                                <n-text tag="b" type="info" class="mr-1 text-2xl">@</n-text>
                                <n-text class="text-lg">{{ userProfile.userinfo.username }}</n-text>
                                <!--签名-->
                                <n-ellipsis :line-clamp="1" class="block w-3/5 sm:hidden ">
                                    <n-text tag="q" type="warning">{{ userProfile.userinfo.signature }}</n-text>
                                </n-ellipsis>

                                <!--分割线-->
                                <n-divider class="mt-2"/>

                                <!--积分-->
                                <n-statistic label="您拥有" tabular-nums>
                                    <n-number-animation
                                            ref="numberAnimationInstRef"
                                            :from="0"
                                            :to="userProfile.userinfo.credit"
                                            precision="2"
                                            class="bg-red-800"
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

                    <!--签名-->
                    <n-ellipsis :line-clamp="1" class="w-30 md:inline-block hidden">
                        {{ userProfile.userinfo.signature }}
                    </n-ellipsis>

                    <!--分割线-->
                    <n-divider class="m-0 bg-zinc-600" vertical/>

                    <!--切换主题按钮-->
                    <n-button class="ms-auto" circle @click="changeTheme(!isDarkTheme)">
                        <n-icon :component="theme.icon"></n-icon>
                    </n-button>

                    <!--消息中心按钮-->
                    <n-badge class="sm:inline-block hidden" dot :offset="[-5.5,5.5]">
                        <n-button circle>
                            <n-icon>
                                <NewspaperOutline/>
                            </n-icon>
                        </n-button>
                    </n-badge>
                </n-flex>
            <div class="md:bg-red-400 sm:bg-sky-200">xxx</div>
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
import {NewspaperOutline} from '@vicons/ionicons5'
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
/*积分数字颜色*/
:deep(.n-statistic-value__content) {
    color: lightcoral !important;
}
</style>
