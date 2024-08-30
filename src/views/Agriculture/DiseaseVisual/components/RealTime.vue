<template>
    <div id="main" ref="chartDom" class="w-full h-[90%]"></div>
</template>
<script setup lang="ts">
import {onMounted, reactive, ref} from 'vue'
import * as echarts from 'echarts';
import {getDiseaseRanking} from "@/apis/disVisual.js";

const chartDom = ref<HTMLDivElement | null>(null)
const myChart = ref<echarts.EChartsType>(null)
const option = reactive({
    xAxis: {
        max: 'dataMax'
    },
    yAxis: {
        type: 'category',
        data: ['玉米叶斑病', '玉米锈病', "玉米叶枯病", '玉米灰斑病', '玉米叶枯病'],
        inverse: true,
        animationDuration: 300,
        animationDurationUpdate: 300,
        max: 5, // only the largest 3 bars will be displayed
        axisLabel: {
            margin: 4,
        }
    },
    series: [
        {
            realtimeSort: true,
            name: '当日数据',
            type: 'bar',
            data: [],
            label: {
                show: true,
                position: 'right',
                valueAnimation: true
            },
            barWidth: '40%'  // 设置条形图的宽度，可以根据需要调整
        }
    ],
    legend: {
        show: true
    },
    animationDuration: 5000,
    animationDurationUpdate: 4000,
    animationEasing: 'linear',
    animationEasingUpdate: 'linear',
    grid: {
        left: '1.5%',
        right: '8.5%', // 右边可以显示到万单位
        containLabel: true
    },
})
onMounted(() => {
    myChart.value = echarts.init(chartDom.value, 'dark')

    setInterval(async function () {
        // 每次间隔都请求一次排名数据, 长轮询
        const res = await getDiseaseRanking()
        let disNames = []
        let disDatas = []
        res.forEach(value => {
            // example:[["玉米灰斑病", 31425], ["玉米叶斑病", 30338], ["玉米锈病", 30196], ["玉米条纹病", 28698], ["玉米叶枯病", 27232]]
            disNames.push(value[0])
            disDatas.push(value[1])
        })
        option.yAxis.data = disNames
        option.series[0].data = disDatas
        option && myChart.value.setOption(option);
    }, 1000);


})


</script>
