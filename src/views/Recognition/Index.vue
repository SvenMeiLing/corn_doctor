<template>
    <n-layout embedded style="border: 1px solid skyblue" class="p-[20px]">
        <n-space :wrap-item="false" :wrap="false">
            <n-grid cols="">
                <n-grid-item>

                </n-grid-item>
            </n-grid>
            <n-space vertical align="start">
                <n-text class="text-4xl font-thin" tag="div">上传植物相片, 以进行即时分析</n-text>
                <n-button color="#20B2AAFF" class="w-[14rem] h-[2.7rem] rounded-tl-xl rounded-br-xl" size="large">
                    <n-text class="text-2xl font-thin">尝试一下</n-text>
                    <n-icon :component="LightbulbTwotone" size="30"></n-icon>
                </n-button>
                <n-text>Upload for Instant Diagnosis
                    <n-text code style="color: palevioletred;">结果将显示在下方表格中:</n-text>
                </n-text>
            </n-space>
            <n-space class="w-1/2" justify="center" align="start">
                <n-steps :current="(current)" :status="currentStatus">
                    <n-step
                            title="上传图片"
                            description="可以是单张或整组的图片"
                    />
                    <n-step
                            title="上传至云"
                            description="云平台会接收并处理您的图片"
                    />
                    <n-step
                            title="结果产出"
                            description="经过我们的模型算法即时反馈结果"
                    />
                </n-steps>
            </n-space>
        </n-space>

        <n-space class="mt-2" vertical style="border: 1px solid red">
            <n-data-table class="shadow-lg rounded-md" :columns="createColumns" :data="data"/>
        </n-space>
        <n-space vertical class="w-1/2">

            <n-space>
                <n-button-group>
                    <n-button @click="prev">
                        <template #icon>
                            <n-icon>
                                <ArrowBackFilled/>
                            </n-icon>
                        </template>
                    </n-button>
                    <n-button @click="next">
                        <template #icon>
                            <n-icon>
                                <ArrowForwardFilled/>
                            </n-icon>
                        </template>
                    </n-button>
                </n-button-group>
                <n-radio-group v-model:value="currentStatus" size="medium" name="basic">
                    <n-radio-button value="error">
                        Error
                    </n-radio-button>
                    <n-radio-button value="process">
                        Process
                    </n-radio-button>
                    <n-radio-button value="wait">
                        Wait
                    </n-radio-button>
                    <n-radio-button value="finish">
                        Finish
                    </n-radio-button>
                </n-radio-group>
            </n-space>
        </n-space>
    </n-layout>

</template>
<script setup>
import {ref} from 'vue'
import {
    LightbulbTwotone,
    ArrowBackFilled,
    ArrowForwardFilled
} from '@vicons/material'

const createColumns = computed(() => {
    return [
        {
            title: '#',
            key: 'num'
        },
        {
            title: '名称',
            key: 'name'
        },
        {
            title: '耗时/置信度',
            key: 'consuming'
        },
        {
            title: '描述',
            key: 'desc'
        }
    ]
})
const data = ref([])

const currentRef = ref(1)

const currentStatus = ref('process')
const current = currentRef
const next = () => {
    if (currentRef.value === null) currentRef.value = 1
    else if (currentRef.value >= 4) currentRef.value = null
    else currentRef.value++
}
const prev = () => {
    if (currentRef.value === 0) currentRef.value = null
    else if (currentRef.value === null) currentRef.value = 4
    else currentRef.value--

}
onMounted(() => {
    data.value.push(
        {
            num: 1,
            name: '...',
            consuming: "...",
            desc: "..."
        }
    )
})

</script>
<style>

</style>
