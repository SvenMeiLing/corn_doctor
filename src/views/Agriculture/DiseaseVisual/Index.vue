<template>
    <n-layout
            :native-scrollbar="false"
            class="p-[20px]"
            ref="containerRef"
            id="visualContainer"
            content-class="w-full h-full"
    >

        <n-space class="w-full h-full p-0 md:flex-nowrap flex-wrap" size="small" :wrap-item="false">
            <!--part1-->
            <div class="min-h-72 sm:h-full md:w-2/5 w-full">
                <div class="h-fit w-full mb-1 md:mb-0 flex items-center">
                    <!--标题-->
                    <n-text class="font-thin text-2xl">平台数据总览</n-text>

                    <!--切换按钮-->
                    <n-text class="text-xl ms-auto text-sky-600 flex items-center cursor-pointer hover:text-sky-900 duration-1000">
                        <n-icon
                        class="ms-auto text-xl"
                        :component="WindStream"
                    ></n-icon>
                        切换为实时数据
                    </n-text>

                </div>

                <!--chart1 -->
                <n-card
                        title=" "
                        class="h-[90%] w-full p-0"
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
                        <n-switch v-show="!loading" class="ms-auto" :rail-style="railStyle">
                            <template #checked>
                                按月显示
                            </template>
                            <template #unchecked>
                                按周显示
                            </template>
                        </n-switch>
                    </template>
                    <!--chart1占位符-->
                    <n-space v-show="loading" vertical class="w-full h-full" :wrap-item="false"
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
                    <div v-show="!loading" id="chart-month" class="h-full w-full"></div>
                    <template #footer>上次更新于{{ dateTime }}</template>
                </n-card>

            </div>

            <!--part2-->
            <n-card class="min-h-72 sm:h-full md:w-3/5 w-full m-0 p-0" content-class="h-full w-full p-2">
                <!--chart2-->
                <div v-show="!loading" id="chart-year" class="h-full w-full"></div>
                <!--chart2占位符-->
                <n-space v-show="loading" class="w-full h-full" align="end" :size="9"
                         :wrap-item="false" :wrap="false">
                    <n-skeleton class="w-[10%] h-[40%]" :sharp="false"/>
                    <n-skeleton class="w-[10%] h-[60%]" :sharp="false"/>
                    <n-skeleton class="w-[10%] h-[30%]" :sharp="false"/>
                    <n-skeleton class="w-[10%] h-[70%]" :sharp="false"/>
                    <n-skeleton class="w-[10%] h-[50%]" :sharp="false"/>
                    <n-skeleton class="w-[10%] h-[90%]" :sharp="false"/>
                    <n-skeleton class="w-[10%] h-[40%]" :sharp="false"/>
                    <n-skeleton class="w-[10%] h-[60%]" :sharp="false"/>
                    <n-skeleton class="w-[10%] h-[80%]" :sharp="false"/>
                    <n-skeleton class="w-[10%] h-[100%]" :sharp="false"/>
                </n-space>
            </n-card>

        </n-space>

    </n-layout>
</template>

<script setup>
import {onMounted, ref} from 'vue'
import * as echarts from 'echarts/core';
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
import {WindStream} from '@vicons/carbon'

import {getAllDiseaseCategory, getDisVisual} from "@/apis/disVisual.js";
import {genDateTime} from '@/utils/genDateTime.js'


const loading = ref(true)
// 本组件内容根容器, 用于检测此区域大小改变以使其图表自适应
const containerRef = ref(null)
// 病害分类及其详情数据
const disCategory = ref([])
// 由病害名称组成的列表
const disNames = ref([])

// 用于展示最后一次数据更新的时间
const dateTime = ref("XXXX-XX-XX")

/**
 * 一个用于返回 style的回调, 由switch组件的切换行为触发
 * @param focused  当前聚焦的选项
 * @param checked  当前选中的选项
 * @return {{}}  样式表
 */
const railStyle = ({
                       focused,
                       checked
                   }) => {
    const style = {};
    if (checked) {
        style.background = "#d03050";
        if (focused) {
            style.boxShadow = "0 0 0 2px #d0305040";
        }
        // 按月显示
        chartWeek("month")
    } else {
        style.background = "#2080f0";

        if (focused) {
            style.boxShadow = "0 0 0 2px #2080f040";
        }
        // 按周显示
        chartWeek("week")
    }
    // 记录数据更新时间
    dateTime.value = genDateTime()
    return style
}

// 有关图表2的额外配置-----------------
const app = {};
const posList = [
    'left',
    'right',
    'top',
    'bottom',
    'inside',
    'insideTop',
    'insideLeft',
    'insideRight',
    'insideBottom',
    'insideTopLeft',
    'insideTopRight',
    'insideBottomLeft',
    'insideBottomRight'
];
app.configParameters = {
    rotate: {
        min: -90,
        max: 90
    },
    align: {
        options: {
            left: 'left',
            center: 'center',
            right: 'right'
        }
    },
    verticalAlign: {
        options: {
            top: 'top',
            middle: 'middle',
            bottom: 'bottom'
        }
    },
    position: {
        options: posList.reduce(function (map, pos) {
            map[pos] = pos;
            return map;
        }, {})
    },
    distance: {
        min: 0,
        max: 100
    }
};
app.config = {
    rotate: 90,
    align: 'left',
    verticalAlign: 'middle',
    position: 'insideBottom',
    distance: 15,
    onChange: function () {
        const labelOption = {
            rotate: app.config.rotate,
            align: app.config.align,
            verticalAlign: app.config.verticalAlign,
            position: app.config.position,
            distance: app.config.distance
        };
        myChart.setOption({
            series: [
                {
                    label: labelOption
                },
                {
                    label: labelOption
                },
                {
                    label: labelOption
                },
                {
                    label: labelOption
                }
            ]
        });
    }
};
const labelOption = {
    show: true,
    position: app.config.position,
    distance: app.config.distance,
    align: app.config.align,
    verticalAlign: app.config.verticalAlign,
    rotate: app.config.rotate,
    formatter: '{c}  {name|{a}}',
    fontSize: 16,
    rich: {
        name: {}
    }
};
//-----------------echarts使用的插件------------------------------------------
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

/**
 * 用于绘制以month/week为分组的图表.
 * @param mode 可以是week或month
 */
async function chartWeek(mode) {
    var chartDom = document.getElementById('chart-month');
    var myChart = echarts.init(chartDom, 'dark');
    var option;
    option = {
        tooltip: {
            trigger: 'axis',
            confine: true // 不超出图表区域
        },
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
    };
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

    option && myChart.setOption(option);

    // 记录数据更新时间
    dateTime.value = genDateTime()
    return myChart
}

/**
 * 用于绘制以年份分组的图表
 * @return {Promise<EChartsType>}
 */
async function chartYear() {
    var chartDom = document.getElementById('chart-year');
    var myChart = echarts.init(chartDom, 'dark');

    let option = {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            data: ['叶斑病', '锈病', '叶枯病', '条纹病', '黑粉病']
        },
        toolbox: {
            show: true,
            orient: 'vertical',
            left: 'right',
            top: 'center',
            feature: {
                mark: {show: true},
                dataView: {show: true, readOnly: false},
                magicType: {show: true, type: ['line', 'bar', 'stack']},
                restore: {show: true},
                saveAsImage: {show: true}
            }
        },
        xAxis: [
            {
                type: 'category',
                axisTick: {show: false},
                data: ['2024', '2025', '2026', '2027', '2028']
            }
        ],
        yAxis: [
            {
                type: 'value'
            }
        ],
        series: [
            // {
            //     name: '叶斑病',
            //     type: 'bar',
            //     barGap: 0,
            //     label: labelOption,
            //     emphasis: {
            //         focus: 'series'
            //     },
            //     data: [320, 332, 301, 334, 390]
            // },
        ]
    };
    // 请求数据
    const resp = await getDisVisual("year")
    // 设置标签
    option.legend.data = Object.keys(resp.datas)
    // 设置x轴数据
    option.xAxis[0].data = resp.year
    // 设置y轴数据
    option.series = Object.keys(resp.datas).map(key => ({
        name: key,
        type: 'bar',
        barGap: 0,
        label: labelOption,  // 使用 labelOption 配置数据标签
        emphasis: {
            focus: 'series'
        },
        data: resp.datas[key]
    }))
    option && myChart.setOption(option);
    return myChart
}


onMounted(async () => {
    // 获取 所有病害名称,并保存待用
    disCategory.value = await getAllDiseaseCategory()
    disNames.value = disCategory.value.map(value => {
        return value.name
    })
    // 初始化图表数据, 调用绘制方法
    let mc = await chartWeek("week")
    let yc = await chartYear()
    // 解除加载状态
    loading.value = false
    // 记录数据更新时间
    dateTime.value = genDateTime()

    const visualContainer = document.querySelector("#visualContainer")
    // 创建 ResizeObserver 实例
    const resizeObserver = new ResizeObserver(() => {
        // 当容器尺寸变化时，重绘制图表
        mc.resize();
        yc.resize();
    });

    // 观察 visualContainer 元素
    resizeObserver.observe(visualContainer);

    const handleNetworkChange = () => {
        if (navigator.onLine) {
            console.log("在线-----")
        }
    };

    window.addEventListener('online', handleNetworkChange);
    window.addEventListener('offline', handleNetworkChange);
})
// todo: 1.未作限流功能,可以持久化数据到客户端的某个地方,下次请求时优先使用客户端存在的数据,每三十分钟更新一次
// todo: 2.每次都会重新初始化渲染图表dom, 待优化方案(深度合并-> 解决配置项多的嵌套配置)
// todo: 3.当前组件或许需要拆分
</script>

<style scoped>

</style>
