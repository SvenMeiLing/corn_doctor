<template>
    <n-layout embedded class="p-[20px] h-full">
        <n-space vertical class="h-full" :wrap-item="false" :size="20">
            <!--header部分-->
            <n-space align="center" size="small" :wrap-item="false" class="w-full h-1/6">
                <n-text
                        class="text-2xl sm:text-2xl lg:text-3xl xl:text-4xl font-thin"
                        type="success"
                        tag="q"
                >
                    病害百科
                </n-text>

                <n-popover trigger="hover">
                    <template #trigger>
                        <n-button quaternary @click="showSearchBox">
                            <template #icon>
                                <n-icon class="mb-1" :component="MenuBookTwotone" :size="'200%'"></n-icon>
                            </template>
                        </n-button>
                    </template>
                    点击可查询
                </n-popover>
                <transition enter-active-class="expand-enter-active"
                            leave-active-class="expand-leave-active"
                            enter-from-class="w-0 opacity-0"
                            leave-to-class="w-0 opacity-0"
                            leave-from-class="w-2/4 opacity-1"
                >
                    <n-select v-if="showBox"
                              class="w-2/4"
                              filterable
                              clearable
                              placeholder="病害搜索"
                              :options="options"
                              v-model:value="selectedValue"
                              @update:value="updateValue"
                    >
                        <template #empty>1</template>
                    </n-select>
                </transition>

            </n-space>
            <n-divider class="h-px m-0 p-0">
                Hi
            </n-divider>

            <!--主体部分-->
            <n-space class="w-full h-4/6" :wrap-item="false" :wrap="false" :size="30">
                <!--病害目录-->
                <n-space :wrap-item="false" :wrap="false" class="w-3/6 h-full" :size="0">
                    <n-scrollbar>
                        <n-collapse @item-header-click="handleItemHeaderClick"
                                    class="w-full h-full"
                                    :expanded-names="doExpand"
                        >
                            <transition-group enter-active-class="animate__animated animate__fadeInRight"
                                              leave-active-class="animate__animated animate__fadeOutRight">
                                <n-collapse-item v-for="(item,index) in filterableDisease" :name="item.src">
                                    <template #header>
                                        <n-text class="lg:text-lg xl:text-xl 2xl:text-2xl">
                                            {{ item.name }}
                                        </n-text>
                                    </template>
                                    <template #default>
                                        <n-blockquote class="ml-5">
                                            <n-tag :bordered="false" type="info" size="small">
                                                病害描述
                                            </n-tag>

                                            <n-text tag="div" class="indent-4">
                                                {{ item.desc }}
                                            </n-text>

                                            <br>
                                            <n-tag :bordered="false" type="success" size="small">
                                                防治手段
                                            </n-tag>
                                            <n-text tag="div" class="indent-4">{{ item.control_methods }}</n-text>
                                            <br>
                                            <n-tag :bordered="false" type="warning" size="small">
                                                常见病发区域/气候
                                            </n-tag>
                                            <n-text tag="div" class="indent-4">{{ item.common }}</n-text>
                                        </n-blockquote>
                                    </template>

                                </n-collapse-item>
                            </transition-group>

                        </n-collapse>
                    </n-scrollbar>
                </n-space>
                <!--病害图片-->
                <n-space :wrap-item="false"
                         :wrap="false"
                         class="w-3/6"
                         justify="center"
                         align="center"
                >
                    <n-image
                            :src="src"
                            width="100%"
                            height="100%"
                            class="w-auto h-full rounded"
                            object-fit="contain"
                            :show-toolbar="false"
                    ></n-image>
                </n-space>
            </n-space>
        </n-space>
    </n-layout>


</template>

<script setup>
import {ref, reactive} from 'vue'
import {MenuBookTwotone} from '@vicons/material';
import 'animate.css'

const diseaseDate = reactive([
    {
        "name": "玉米条纹病毒",
        "desc": "玉米条纹病毒是一种通过蚜虫传播的病毒病，导致玉米叶片出现黄白色条纹，影响光合作用和植株生长。",
        "control_methods": "种植抗病品种，控制蚜虫，使用杀虫剂进行防治，及时清除病株。",
        "common": "常见于温暖、湿润的地区，尤其在春季和夏季高发。",
        "src": "/src/assets/corn_category/msv.jpg"
    },
    {
        "name": "叶枯病",
        "desc": "叶枯病由多种病原菌引起，导致玉米叶片上出现褐色斑点，斑点逐渐扩大并融合，最终导致叶片干枯。",
        "control_methods": "加强田间管理，保持良好的通风透光条件，使用适当的杀菌剂。",
        "common": "在高温高湿的环境下，尤其是雨季容易发生。",
        "src": "/src/assets/corn_category/blight.jpg"
    },
    {
        "name": "玉米灰斑病",
        "desc": "玉米灰斑病主要由真菌引起，病斑呈灰褐色，边缘有黄色晕圈，会影响玉米的光合作用。",
        "control_methods": "轮作种植，避免连作，及时清除田间残留物，使用防治真菌的药剂。",
        "common": "多发于温暖潮湿的地区，尤其在夏季和早秋高发。",
        "src": "/src/assets/corn_category/gls_32.jpg"
    },
    {
        "name": "玉米褐斑病",
        "desc": "玉米褐斑病也是由真菌引起，症状包括叶片上出现褐色病斑，严重时会导致叶片枯死。",
        "control_methods": "选择抗病品种，合理密植，使用杀菌剂进行防治。",
        "common": "常见于温暖潮湿的环境，在夏季和秋季易发生。",
        "src": "/src/assets/corn_category/bs.jpg"

    },
    {
        "name": "玉米锈病",
        "desc": "玉米锈病由锈菌引起，病斑呈现锈红色粉状斑点，严重感染会导致叶片早期枯黄。",
        "control_methods": "选择抗病品种，及时清理病残体，使用针对性的杀菌剂。",
        "common": "多发于高湿度条件下，特别是在夏末和秋初。",
        "src": "/src/assets/corn_category/rust.jpg"
    },
    {
        "name": "玉米黑粉病",
        "desc": "玉米黑粉病由真菌引起，玉米果穗和茎部会形成黑色粉状孢子团，影响产量和品质。",
        "control_methods": "种植抗病品种，拔除病株并进行深埋处理，使用适当的杀菌剂。",
        "common": "在温暖潮湿的气候条件下，特别是在生长期易爆发。",
        "src": "/src/assets/corn_category/smut.jpg"
    },
    {
        "name": "玉米霜霉病",
        "desc": "玉米霜霉病由霜霉菌引起，病斑通常呈水渍状，叶片背面可见白色霉层，严重时导致植株死亡。",
        "control_methods": "选择抗病品种，合理轮作，喷洒防霉剂。",
        "common": "多发于凉爽潮湿的天气，尤其在春季和秋季。",
        "src": "/src/assets/corn_category/mildew.jpg"
    },
    {
        "name": "草地贪夜蛾病",
        "desc": "草地贪夜蛾是一种侵食性强的害虫，其幼虫对玉米植株的叶片和果穗造成严重破坏。",
        "control_methods": "使用生物防治和化学防治相结合的方法，如释放天敌和喷洒杀虫剂。",
        "common": "在温暖干燥的地区全年都有发生，尤以夏季为甚。",
        "src": "/src/assets/corn_category/fal.jpg"
    },
    {
        "name": "健康",
        "desc": "健康的玉米植株生长旺盛，叶片绿色无病斑，果穗饱满。",
        "control_methods": "加强田间管理，预防病虫害，合理施肥灌溉。",
        "common": "适用于所有玉米种植地区和季节。",
        "src": "/src/assets/corn_category/healthy.jpg"
    },
    {
        "name": "三化螟",
        "desc": "三化螟是一种钻蛀性害虫，其幼虫啃食玉米茎秆，导致植株倒伏，影响产量。",
        "control_methods": "使用生物防治如天敌昆虫，结合化学防治如喷洒杀虫剂。",
        "common": "常在温暖湿润的地区发生，尤其在夏季和秋季。",
        "src": "/src/assets/corn_category/ysb.jpg"
    },
    {
        "name": "三化螟幼虫",
        "desc": "三化螟幼虫是三化螟的幼虫阶段，对玉米茎秆和叶片具有很强的啃食能力。",
        "control_methods": "采取早期监测和及时防治措施，使用生物和化学防治方法。",
        "common": "在温暖湿润的环境中，夏季和秋季是高发期。",
        "src": "/src/assets/corn_category/tsbl.jpg"
    },
    {
        "name": "小核盘菌叶斑病",
        "desc": "小核盘菌叶斑病由真菌引起，病斑呈圆形或不规则形，颜色由浅褐到深褐不等，严重时导致叶片枯死。",
        "control_methods": "及时清除病叶，适当密植，使用防治真菌的杀菌剂。",
        "common": "多发于潮湿和温暖的环境，尤其在春季和秋季。",
        "src": "/src/assets/corn_category/mlb.jpg"
    },
    {
        "name": "北方叶枯病",
        "desc": "北方叶枯病多由真菌引起，症状包括叶片出现不规则褐色病斑，严重时叶片早期枯死。",
        "control_methods": "选择抗病品种，加强田间管理，使用适当的杀菌剂。",
        "common": "主要发生在北方玉米种植区，尤其在夏季和秋季。",
        "src": "/src/assets/corn_category/nlb.jpg"
    },
    {
        "name": "南方叶斑病",
        "desc": "南方叶斑病主要在南方玉米产区发生，病斑呈现褐色或黑色，严重影响光合作用和产量。",
        "control_methods": "种植抗病品种，合理轮作，及时进行药剂防治。",
        "common": "多发于南方地区，尤其在温暖潮湿的季节，如夏季和秋季。",
        "src": "/src/assets/corn_category/nls.jpg"
    }
])
const showBox = ref(false)

const src = ref("/src/assets/corn_category/corn-health.jpg")

const showSearchBox = () => {
    // 显示搜索框
    showBox.value = !showBox.value
    // 点击按钮清空过滤
    selectedValue.value = void 0
}

const selectedValue = ref(null)

const doExpand = ref([])
const updateValue = () => {
    // 当选项发生变化,切换对应图片
    diseaseDate.forEach(value => {
        if (value.name === selectedValue.value) {
            src.value = value.src
        }
    })
    setTimeout(() => {
        // 延迟0.5s后展开
        doExpand.value.push(src.value)
    }, 500)

}
const options = computed(() =>
    // 设置可选病害
    diseaseDate.map((value) => {
        console.log(value)
        return {label: value.name, value: value.name}
    })
)


// 点击某个病害名称,切换src的链接,通过传递src -> name
const handleItemHeaderClick = ({
                                   name,
                                   expanded
                               }) => {
    // 切换图片
    src.value = name
    if (!expanded) {
        // 这般我也不知道为什么这样写,因为!expanded意思是非展开, 所有应该展开我也不知道为什么要关闭
        // 与正常逻辑相反
        const index = doExpand.value.findIndex(el => el === name)
        if (index > -1) {
            doExpand.value.splice(index, 1)
        }
    } else {
        doExpand.value.push(name)
    }

};

const filterableDisease = computed(() => {
    if (selectedValue.value) {
        console.log("has avlue")
        return diseaseDate.filter((value) => value.name === selectedValue.value)
    } else {
        return diseaseDate
    }

})
watch(selectedValue, (nv) => {
    console.log(nv)
})
onMounted(() => {
    console.log(options)
})
</script>
<style>
/* 定义进入和离开状态的初始和结束状态 */
.expand-enter-active, .expand-leave-active {
    transition: all 0.5s ease;
}

.expand-enter-from, .expand-leave-to {
    width: 0;
    opacity: 0; /* 可选：也可以改变透明度 */
}

.expand-enter-to, .expand-leave-from {
    width: 50%;
    opacity: 1; /* 可选：也可以改变透明度 */
}
</style>
