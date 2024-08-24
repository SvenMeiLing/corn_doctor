<template>
    <div id="main" class="w-full h-[90%]"></div>
</template>
<script setup>
import {onMounted, nextTick} from 'vue'
import * as echarts from 'echarts/core';
import {
    GraphicComponent,
    GridComponent,
    LegendComponent, TitleComponent, ToolboxComponent, TooltipComponent
} from 'echarts/components';
import {BarChart, LineChart} from 'echarts/charts';
import {CanvasRenderer} from 'echarts/renderers';
import {LabelLayout, UniversalTransition} from "echarts/features";

echarts.use([
    GraphicComponent,
    GridComponent,
    LegendComponent,
    BarChart,
    CanvasRenderer,
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

onMounted(() => {
    nextTick(() => {
        var chartDom = document.getElementById('main');
        var myChart = echarts.init(chartDom, "dark");

        var option;

        const rawData = [
            [100, 302, 301, 334, 390, 330, 320],
            [320, 132, 101, 134, 90, 230, 210],
            [220, 182, 191, 234, 290, 330, 310],
            [150, 212, 201, 154, 190, 330, 410],
            [820, 832, 901, 934, 1290, 1330, 1320]
        ];

// 选择需要显示的列索引，例如当天的数据
        const dayIndex = 6; // 这里选择的是第7列数据（索引为6）

        const categoryData = ['玉米叶斑病', '玉米锈病', '玉米叶枯病', '玉米条纹病毒', '玉米灰斑病'];
        const dataForDay = rawData.map((data) => data[dayIndex]);

// 为了显示排序后的数据，生成排序后的数据和标签
        const sortedData = dataForDay.map((value, index) => ({
            name: categoryData[index],
            value
        })).sort((a, b) => b.value - a.value);

        const series = [{
            name: '病害数量',
            type: 'bar',
            data: sortedData.map((item) => item.value),
            label: {
                show: true,
                position: 'top',
                formatter: (params) => Math.round(params.value * 1000) / 10 + '%'
            }
        }];

        option = {
            legend: {
                selectedMode: false
            },
            grid: {
                left: 50,
                right: 50,
                top: 50,
                bottom: 50
            },
            yAxis: {
                type: 'value'
            },
            xAxis: {
                type: 'category',
                data: sortedData.map((item) => item.name)
            },
            series
        };

        option && myChart.setOption(option);
    })

})


</script>
