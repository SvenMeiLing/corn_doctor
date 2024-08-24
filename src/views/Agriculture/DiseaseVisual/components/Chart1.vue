<template>
  <!--part1-->
    <div class="w-full h-[90%]">

        <!--chart1 -->
        <n-card
                title=" "
                class="h-full w-full p-0"
                content-class="h-full w-full p-2 pt-0"
                header-class="p-1 pr-2"
                header-extra-class="w-full ps-2"
                footer-class="font-thin text-zinc-400"
        >

            <template #header-extra>

                <!--title占位符-->
                <span v-show="loading" class="animate-ping bg-red-200 rounded-full w-2 h-2 opacity-75"></span>
                <n-text class="ms-3" v-show="loading">
                    正在加载中......
                </n-text>
                <n-skeleton v-show="loading" class="w-20 h-5 ms-auto" round/>

                <!--title内容-->
                <n-switch v-show="!loading" class="ms-auto" @update:value="switchMode">
                    <template #checked>
                        按月显示
                    </template>
                    <template #unchecked>
                        按周显示
                    </template>
                </n-switch>
            </template>
            <!--chart1占位符-->
            <n-space
                    v-show="loading"
                    vertical class="w-full h-full"
                    :wrap-item="false"
                    :wrap="false"
            >
                <n-skeleton class="w-full h-1/6" :sharp="false"/>
                <n-skeleton class="w-full h-1/6" :sharp="false"/>
                <n-skeleton class="w-full h-1/6" :sharp="false"/>
                <n-skeleton class="w-full h-1/6" :sharp="false"/>
                <n-skeleton class="w-full h-1/6" :sharp="false"/>
                <n-skeleton class="w-full h-1/6" :sharp="false"/>
            </n-space>

            <!--chart1内容-->
            <div v-show="!loading" ref="chartDom" class="w-full h-full"></div>

            <template #footer>上次更新于{{ dateTime }}</template>

        </n-card>

    </div>

</template>

<script setup lang="ts">
import {ref, reactive, onMounted, nextTick} from "vue";
import {
    TitleComponent,
    ToolboxComponent,
    TooltipComponent,
    GridComponent,
    LegendComponent,
} from 'echarts/components';
import {LineChart, BarChart} from 'echarts/charts';
import {UniversalTransition, LabelLayout} from 'echarts/features';
import {CanvasRenderer} from 'echarts/renderers';
import {WindStream} from "@vicons/carbon";
import * as echarts from "echarts/core";
import {getAllDiseaseCategory, getDisVisual} from "@/apis/disVisual.js";
import {genDateTime} from "@/utils/genDateTime.js";


echarts.use([
    TitleComponent,
    ToolboxComponent,
    TooltipComponent,
    GridComponent,
    LegendComponent,
    LineChart,
    CanvasRenderer,
    UniversalTransition,
    BarChart,
    LabelLayout
]);

// 图表dom元素
const chartDom = ref<HTMLDivElement | null>(null)
// 图表实例对象
const myChart = ref<EChartsType | null>(null)
const loading = ref(true)
const checked = ref(false)
// 病害分类及其详情数据
const disCategory = ref([])
// 由病害名称组成的列表
const disNames = ref([])
// 用于展示最后一次数据更新的时间
const dateTime = ref("XXXX-XX-XX")
// 读取store中主题配置
import {useDesignSettingStore} from "@/stores/designSetting.js";
import {storeToRefs} from 'pinia'
import {EChartsType} from 'echarts'

const themeStore = useDesignSettingStore()
const {theme} = storeToRefs(themeStore)


const switchMode = (value) => {
    // value默认false也就是周, 可以换成month
    console.log(value)
    if (value) {
        // 表示从周切换到月
        updateChart("month")
    } else {
        updateChart("week")
    }
    checked.value = !checked.value

}
const option = reactive({
    animationDuration: 5000,
    animationDurationUpdate: 2000,
    legend: {
        data: ['玉米叶斑病', '玉米锈病', '玉米叶枯病', '玉米条纹病', '玉米黑粉病']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['周一', '周二', '周三', '周四', '周五', '周六', '周天']
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name: '玉米叶斑病',
            type: 'line',
            stack: 'Total',
            data: [120, 132, 101, 134, 90, 230, 210]
        }
    ]
})

/**
 * 用于绘制以month/week为分组的图表.
 * @param mode 可以是week或month
 * @param chartDom 图表的dom对象
 */
async function initChart(mode, chartDom) {
    // 提前取消加载状态,否则echarts无法及时获取元素宽高造成渲染图表过小的bug
    loading.value = false
    await updateChart(mode)
    // 初始化操作晚一些执行,等待dom加载完成
    myChart.value = echarts.init(chartDom, "dark");
    option && myChart.value.setOption(option);
    return myChart
}

/**
 * 更新图表数据
 * @param mode 可可选week,month
 * @return {Promise<void>}
 */
async function updateChart(mode) {
    // 请求数据
    const resp = await getDisVisual(mode)
    // 设置标签
    option.legend.data = disNames.value
    // 设置x轴数据
    option.xAxis.data = resp[mode]
    // 设置y轴数据
    option.series = Object.keys(resp.datas).map(key => ({
        name: key,
        type: 'line',
        stack: 'Total',
        data: resp.datas[key]
    }))

    // 添加没用出现的病害类别， 并初始化data为全是0的数组
    for (let disName of disNames.value) {
        option.series.push(
            {
                name: disName,
                type: 'line',
                stack: 'Total',
                data: [0, 0, 0, 0, 0, 0, 0]
            }
        )
    }
    myChart.value?.setOption(option)
    // 记录数据更新时间
    dateTime.value = genDateTime()

}

onMounted(async () => {
    disCategory.value = await getAllDiseaseCategory()
    disNames.value = disCategory.value.map(value => {
        return value.name
    })
    await nextTick(async () => {
        await initChart("week", chartDom.value)
    })
})


</script>

<style scoped>

</style>
