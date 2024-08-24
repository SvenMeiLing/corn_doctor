<template>
    <n-card class="min-h-72 sm:h-full md:w-3/5 w-full m-0 p-0" content-class="h-full w-full p-2">
        <!--chart2-->
        <div v-show="!loading" ref="chartDom" class="h-full w-full"></div>
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
</template>

<script setup>
import {ref, onMounted, reactive} from "vue";
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
import {getDisVisual} from "@/apis/disVisual.js";

const loading = ref(true)
const myChart = ref(null)
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
const chartDom = ref(null)
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
const option = reactive({
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
    series: []
});
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
 * 用于绘制以年份分组的图表
 * @return {Promise<EChartsType>}
 */
async function chartYear() {

    loading.value = false
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
    myChart.value = echarts.init(chartDom.value, 'dark');
    option && myChart.value.setOption(option);
    return myChart
}

onMounted(async () => {
    await nextTick(async() => {
        await chartYear()
    })

})
</script>

<style scoped>

</style>
