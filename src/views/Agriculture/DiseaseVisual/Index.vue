<template>
    <n-layout
            :native-scrollbar="false"
            class="p-[20px]"
            ref="containerRef"
            id="visualContainer"
            content-class="w-full h-full"
    >
        <n-space class="w-full h-full p-0" :wrap-item="false" :wrap="false">
            <div id="chart-month" class="h-1/2 w-2/5"></div>
            <div id="chart-year" class="h-full w-3/5"></div>
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
import {getAllDiseaseCategory, getDisVisual} from "@/apis/disVisual.js";


const containerRef = ref(null)
const disCategory = ref([])
const disNames = ref([])
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
//-----------------------------------------------------------
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

async function chartWeek() {
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
    const resp = await getDisVisual("week")
    // 设置标签
    option.legend.data = disNames.value
    // 设置x轴数据
    option.xAxis.data = resp.week
    // 设置y轴数据
    option.series = Object.keys(resp.datas).map(key => ({
        name: key,
        type: 'line',
        stack: 'Total',
        data: resp.datas[key]
    }))

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
    return myChart
}

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
    disCategory.value = await getAllDiseaseCategory()
    // 所有病害名称
    disNames.value = disCategory.value.map(value => {
        return value.name
    })
    console.log(disNames.value, "<---log")
    let mc = await chartWeek()
    let yc = await chartYear()
    const visualContainer = document.querySelector("#visualContainer")
    // 创建 ResizeObserver 实例
    const resizeObserver = new ResizeObserver(() => {
        console.log("重新绘制");
        // 当容器尺寸变化时，重绘制图表
        mc.resize();
        yc.resize();
    });

    // 观察 visualContainer 元素
    resizeObserver.observe(visualContainer);


    // 绘制
    // option && yc.setOption(option)


})
/*
类别:[叶斑病, 叶枯病]
年份:[2023,2024]
数据:[200,300]
data = [
    {name:叶斑病, year:[2024, 2025, 2026], total:[22, 445, 355]},
    {name:叶枯病, year:[2024, 2025, 2026], total:[22, 445, 355]},
]
 */

</script>

<style scoped>

</style>
