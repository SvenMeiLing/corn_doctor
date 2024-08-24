<template>
    <n-layout
            :native-scrollbar="false"
            class="p-[20px]"
            ref="containerRef"
            id="visualContainer"
            content-class="w-full h-full"
    >
        <!--内容容器-->
        <n-space
                class="w-full h-full p-0 md:flex-nowrap flex-wrap"
                size="small" :wrap-item="false">
            <div class="min-h-72 sm:h-full md:w-2/5 w-full">
                <!--title-->
                <div class="h-[10%] w-full mb-1 md:mb-0 flex items-center">
                    <!--标题-->
                    <n-text class="font-thin text-2xl">平台数据总览</n-text>

                    <!--切换按钮-->
                    <n-text
                            class="text-xl ms-auto text-sky-600 flex bg-zinc-700 rounded-md p-1 items-center cursor-pointer
                hover:bg-zinc-600 duration-1000 active:p-2"
                            @click="toggleComponent">
                        <n-icon
                                class="ms-auto text-xl"
                                :component="WindStream"
                        ></n-icon>
                        {{ isRealTime ? '切换为一周数据' : '切换为实时数据' }}
                    </n-text>

                </div>

                <!--part1-->
                <transition name="fade" mode="in-out"
                >
                    <component :is="activeComponent"></component>
                </transition>

            </div>

            <!--part2-->
            <Chart2></Chart2>
        </n-space>

    </n-layout>
</template>

<script setup>
import {onMounted, ref, computed, shallowRef} from 'vue'

import Chart1 from "@/views/Agriculture/DiseaseVisual/components/Chart1.vue";
import Chart2 from "@/views/Agriculture/DiseaseVisual/components/Chart2.vue";
import {WindStream} from "@vicons/carbon";
import RealTime from "@/views/Agriculture/DiseaseVisual/components/RealTime.vue";


const containerRef = ref(null)
const activeComponent = shallowRef(Chart1)

const isRealTime = ref(false)
const toggleComponent = () => {
    // 切换组件
    activeComponent.value = activeComponent.value === Chart1 ? RealTime : Chart1
    isRealTime.value = !isRealTime.value
}

onMounted(async () => {
    // const visualContainer = document.querySelector("#visualContainer")
    // // 创建 ResizeObserver 实例
    // const resizeObserver = new ResizeObserver(() => {
    //     // 当容器尺寸变化时，重绘制图表
    //     mc.resize();
    //     yc.resize();
    // });
    //
    // // 观察 visualContainer 元素
    // resizeObserver.observe(visualContainer);
})
// todo: 1.未作限流功能,可以持久化数据到客户端的某个地方,下次请求时优先使用客户端存在的数据,每三十分钟更新一次
// todo: 2.每次都会重新初始化渲染图表dom, 待优化方案(深度合并-> 解决配置项多的嵌套配置)
// todo: 3.当前组件或许需要拆分
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>
