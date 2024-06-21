<template>
    <n-space vertical class="h-4/6"  :wrap="true" :wrap-item="false">
        <n-data-table bordered class="shadow-lg rounded-md h-full" :columns="createColumns"
                      :data="data" :flex-height="true">
            <template #empty>
                <n-empty size="large">
                    <template #icon>
                        <n-image preview-disabled class="h-full w-full" src="src/assets/images/table.png"></n-image>
                    </template>
                    <template #extra>
                        哦!你还没有上传图片呢?
                    </template>
                </n-empty>
            </template>
        </n-data-table>
    </n-space>
</template>

<script setup>
import {onMounted, computed, ref, onUnmounted} from "vue";
import emitter from "@/utils/mitt.js";


const createColumns = computed(() => {
    return [
        {
            title: '#',
            key: 'id'
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
const data = ref([
    // {
    //     id: 1,
    //     name: '...',
    //     consuming: "...",
    //     desc: "..."
    // }
])

onMounted(() => {
    emitter.on('recognitionData', (recognitionData) => {
        // 如果有数据传递才去渲染,没有则不渲染
        if (recognitionData) {
            console.log(recognitionData)
            data.value = recognitionData?.map((value, index) => {
                return {
                    id: index + 1,
                    ...value
                }
            })
        } else {
            console.log('没有数据了')
        }

    })
})
onActivated(() => {
    console.log('我是子组件')
})
// 移除
onUnmounted(() => {
    console.log("TableView to onUnMounted")
    emitter.off('recognitionData', () => {
    })
})
</script>
