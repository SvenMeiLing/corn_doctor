<template>
    <n-space vertical class="h-4/6" :wrap="true" :wrap-item="false">
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
import {NImage, NTag, NPopover} from "naive-ui";


const createColumns = computed(() => {
    return [
        {
            title: '#',
            key: 'id'
        },
        {
            title: '图像',
            key: 'media_url',
            render(row) {
                return h(NImage, {
                    src: row.media_url,
                    // style:"width:100px;height:100px",
                    "class": "w-16 h-16"
                })
            }
        },
        {
            title: '所患病害',
            key: 'disease',
            render(row) {
                let tags = []
                for (const dis of row.diseases) {
                    tags.push(
                        h(NPopover,
                            {
                                placement: 'top',
                                trigger: 'hover'
                            },
                            {
                                default: () => [  // tag-popover
                                    h("div", null, [h("span", {class: "text-lg "}, "描述: "), h("span", {class: "decoration-solid underline text-base"}, `${dis.description}`)]),
                                    h("div", null, [h("span", {class: "text-lg "}, "病因: "), h("span", {class: "decoration-solid underline text-base"}, `${dis.cause}`)]),
                                    h("div", null, [h("span", {class: "text-lg "}, "特征: "), h("span", {class: "decoration-solid underline text-base"}, `${dis.symptom}`)]),
                                    h("div", null, [h("span", {class: "text-lg "}, "防治手段: "), h("span", {class: "decoration-solid underline text-base"}, `${dis.preventive_measure}`)]),
                                    h("div", null, [h("span", {class: "text-lg "}, "影响程度: "), h("span", {class: "decoration-solid underline text-base"}, `${dis.impact}`)]),

                                ],
                                trigger: () => h(NTag, {
                                    type: "warning", class: "m-1"
                                }, {
                                    default: () => dis.name
                                })
                            }
                        )
                    )
                    // tags.push(h(NTag, {
                    //     type: "warning",
                    //     class: "m-1"
                    // }, {
                    //     default: () => dis.name
                    // }))
                }
                return tags
            }
        }
    ]
})
const data = ref([
    // {
    //     id: 1,
    //     media_url: "http://127.0.0.1:8000/predict/2024/7/4/3058a01abb0eb8a9a62379c17e3ba6d4.webp",
    //     diseases: [
    //         {
    //             name: "玉米叶斑病", impact: "高",
    //             description: "玉米灰斑病（Gray leaf spot）是一种真菌性病害。",
    //             symptom: "叶片上出现灰色至棕色长条形斑点，严重时导致叶片枯死。",
    //             cause: "由真菌Cercospora zeae-maydis引起，在温暖潮湿条件下易爆发。",
    //             preventive_measure: "使用抗病品种，轮作，减少田间湿度，及时喷洒杀菌剂。"
    //         },
    //         {
    //             name: "北方叶枯病", impact: "高",
    //             description: "玉米灰斑病（Gray leaf spot）是一种真菌性病害。",
    //             symptom: "叶片上出现灰色至棕色长条形斑点，严重时导致叶片枯死。",
    //             cause: "由真菌Cercospora zeae-maydis引起，在温暖潮湿条件下易爆发。",
    //             preventive_measure: "使用抗病品种，轮作，减少田间湿度，及时喷洒杀菌剂。"
    //         },
    //         {
    //             name: "南方叶斑病", impact: "高",
    //             description: "玉米灰斑病（Gray leaf spot）是一种真菌性病害。",
    //             symptom: "叶片上出现灰色至棕色长条形斑点，严重时导致叶片枯死。",
    //             cause: "由真菌Cercospora zeae-maydis引起，在温暖潮湿条件下易爆发。",
    //             preventive_measure: "使用抗病品种，轮作，减少田间湿度，及时喷洒杀菌剂。"
    //         }
    //     ]
    // }
])

onMounted(() => {
    emitter.on('recognitionData', (recognitionData) => {
        // 如果有数据传递过来才去渲染,没有则不渲染
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
