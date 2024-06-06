<template>
    <n-layout embedded style="border: 1px solid skyblue" class="p-[20px]">
        <n-space :wrap-item="false" :wrap="false">
            <n-grid cols="1 s:1 m:2 xl:2" responsive="screen" style="border: 1px solid lightgreen">
                <n-grid-item style="border: 1px solid lightgreen">
                    <n-space vertical align="start">
                        <n-text class="text-4xl font-thin" tag="div">上传植物相片, 以进行即时分析</n-text>
                        <n-button color="#20B2AAFF" class="w-[14rem] h-[2.7rem] rounded-tl-xl rounded-br-xl"
                                  size="large"
                                  @click="showModal = true"
                        >
                            <n-text class="text-2xl font-extralight  dark:text-black ">尝试一下</n-text>
                            <n-icon :component="LightbulbTwotone" size="30" class="bulb"></n-icon>
                        </n-button>
                        <n-modal
                                v-model:show="showModal"
                                class="custom-card"
                                preset="card"
                                :style="bodyStyle"
                                size="huge"
                                :bordered="false"
                                :segmented="segmented"
                        >
                            <template #header>
                                <n-space align="center" class="h-full" size="small"
                                         :wrap-item="false">
                                    <img src="/src/assets/images/smile.png"
                                         class="h-9" alt="">
                                    <n-text class="font-thin">
                                        仅支持图片文件哦!
                                    </n-text>
                                </n-space>

                            </template>

                            <n-form
                                    ref="formRef"
                                    inline
                                    :label-width="80"
                                    :model="formValue"
                                    :rules="rules"
                            >
                                <n-form-item label="Upload" path="formValue">
                                    <n-upload multiple
                                              :create-thumbnail-url="createThumbnailUrl"
                                              list-type="image"
                                    >
                                        <n-button @click="logFile">Upload file</n-button>
                                    </n-upload>
                                </n-form-item>


                            </n-form>


                            <template #footer>
                                尾部
                            </template>
                        </n-modal>
                        <n-text>Upload for Instant Diagnosis
                            <n-text code style="color: palevioletred;">结果将显示在下方表格中:</n-text>
                        </n-text>
                    </n-space>
                </n-grid-item>
                <n-grid-item style="border: 1px solid lightgreen">

                </n-grid-item>
            </n-grid>


        </n-space>

        <n-space class="mt-2" vertical style="border: 1px solid red">
            <n-data-table class="shadow-lg rounded-md" :columns="createColumns" :data="data"/>
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

const showModal = ref(false)
const bodyStyle = {
        width: "600px"
    },
    segmented = {
        content: "soft",
        footer: "soft"
    }
const formValue = reactive({
        files: []
    }),
    rules = reactive({
        files: {
            required: true,
            trigger: 'blur'
        }
    }),
    logFile = () => {
        console.log(formValue.files)
    },
    createThumbnailUrl1 = (file) => {
        return file
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
<style scoped>
#dark .bulb {
    filter: drop-shadow(0 -5px 4px yellow)
}
</style>
