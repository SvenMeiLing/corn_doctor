<script setup>
import {ref} from 'vue'
import {
    LightbulbTwotone,
    DriveFolderUploadFilled
} from '@vicons/material'
import {uploadImg} from "@/apis/recognition.js";
import {useLoadingBar} from 'naive-ui'

const loadingBar = useLoadingBar()
const zzy = ref(null)

const showModal = ref(false)
const segmented = {
    content: "soft",
    footer: "soft"
}

const userFiles = ref([]),
    uploadRef = ref(),
    handleClick = async () => {
        window.$loadingBar.start()
        const formData = new FormData()
        userFiles.value.forEach((value, index) => {
            // console.log(value.file)
            formData.append('file', value.file)
        })
        // const res = await uploadImg(formData)
        // loadingBar.finish()
    },
    // defaultFList = reactive([
    //     {
    //         id: 'razars',
    //         name: '刀.png',
    //         status: 'finished',
    //         url: "https://picsum.photos/50/50"
    //     },
    //     {
    //         id: 'edge',
    //         name: '锋.png',
    //         status: 'finished',
    //         url: "https://picsum.photos/50/50"
    //     },
    //     {
    //         id: 'razars',
    //         name: '剑.png',
    //         status: 'finished',
    //         url: "https://picsum.photos/50/50"
    //     },
    //     {
    //         id: 'edge',
    //         name: '客.png',
    //         status: 'finished',
    //         url: "https://picsum.photos/50/50"
    //     },
    //     {
    //         id: 'razars',
    //         name: '刀.png',
    //         status: 'finished',
    //         url: "https://picsum.photos/50/50"
    //     },
    //     {
    //         id: 'edge',
    //         name: '锋.png',
    //         status: 'finished',
    //         url: "https://picsum.photos/50/50"
    //     },
    //     {
    //         id: 'razars',
    //         name: '剑.png',
    //         status: 'finished',
    //         url: "https://picsum.photos/50/50"
    //     },
    //     {
    //         id: 'edge',
    //         name: '客.png',
    //         status: 'finished',
    //         url: "https://picsum.photos/50/50"
    //     }
    // ]),
    beforeUpload = (data) => {
        console.log(data)
    },
    fileListUpdate = (fileList) => {
        userFiles.value = fileList
        console.log(userFiles.value)
    },
    onFinish = (file, event) => {
        console.log("finish")
    }
// todo: 点击上传后,选择文件,最后提交发起请求form-data,等待服务器响应,关闭对话框渲染数据到表格中

</script>

<template>
    <n-loading-bar-provider :to="zzy">
        <n-space :wrap-item="false" :wrap="false">
        <n-grid cols="1 s:1 m:2 xl:2" responsive="screen" style="border: 1px solid lightgreen">
            <n-grid-item style="border: 1px solid lightgreen">
                <n-space vertical align="start">

                    <n-text ref="zzy" class="text-4xl font-thin" tag="div">上传植物相片, 以进行即时分析</n-text>
                    <n-button color="#20B2AAFF" class="w-[14rem] h-[2.7rem] rounded-tl-xl rounded-br-xl"
                              size="large"
                              @click="showModal = true"
                    >
                        <n-text class="text-2xl font-extralight  dark:text-black ">尝试一下</n-text>
                        <n-icon :component="LightbulbTwotone" size="30" class="bulb"></n-icon>
                    </n-button>

                    <n-modal
                            to=".n-config-provider"
                            v-model:show="showModal"
                            class="custom-card w-96 sm:w-96 md:w-4/6 xl:w-1/2"
                            preset="card"
                            size="huge"
                            :bordered="false"
                            :segmented="segmented"
                            content-class="p-0"
                    >
                        <template #header>

                            <n-space

                                    align="center"
                                    class="sp h-full"
                                    size="small"
                                    :wrap-item="false"
                            >

                                <img src="/src/assets/images/smile.png"
                                     class="h-9" alt="">
                                <n-text class="font-thin">
                                    仅支持图片文件哦!
                                </n-text>
                            </n-space>


                        </template>

                        <!--type为file的input-->

                        <n-upload
                                ref="uploadRef"
                                action="http://127.0.0.1:8000/upload"
                                multiple
                                :file-list="userFiles"
                                @update:file-list="fileListUpdate"
                                list-type="image"
                                file-list-class="file-list flex flex-wrap overflow-auto
                                          max-h-[6rem] bg-rose-100/75 dark:bg-rose-900/50 rounded shadow-md dark:shadow-rose-900/50"
                                class="flex flex-col "
                                accept="image/*"
                        >
                            <n-button>
                                <n-icon :size="25" :component="DriveFolderUploadFilled"></n-icon>
                                上传植物图片
                            </n-button>

                        </n-upload>

                        <template #footer>
                            <n-button
                                    :disabled="0"
                                    style="margin-bottom: 12px"
                                    @click="handleClick"
                            >
                                提交
                            </n-button>
                        </template>
                    </n-modal>
                    <n-text>Upload for Instant Diagnosis
                        <n-text code style="color: palevioletred;">结果将显示在下方表格中:</n-text>
                    </n-text>
                </n-space>
            </n-grid-item>
        </n-grid>


    </n-space>
    </n-loading-bar-provider>

</template>


<style scoped>
#dark .bulb {
    /*黑暗模式时灯泡会亮*/
    filter: drop-shadow(0 -5px 4px yellow)
}

:deep(.file-list::-webkit-scrollbar) {
    width: 5px; /* 设置滚动条宽度 */
}

:deep(.file-list::-webkit-scrollbar-thumb) {
    background-color: #888; /* 设置滚动条手柄的背景颜色 */
    border-radius: 7px; /* 设置滚动条手柄的圆角 */
}

:deep(.file-list::-webkit-scrollbar-track) {
    background-color: transparent; /* 设置滚动条轨道的背景颜色 */
}

:deep(.n-upload-file) {
    flex-grow: 1;
}
</style>
