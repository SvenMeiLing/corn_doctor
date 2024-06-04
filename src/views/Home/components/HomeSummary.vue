<template>
    <n-scrollbar class="
        h-full
        xl:max-h-[30rem]
        xl:min-h-[27rem]
        2xl:max-h-[39rem]"
    >
        <n-layout class="h-full" embedded content-class="p-[20px] h-full xl:min-h-[27.5rem]" content-style="border:1px solid red">
            <n-space justify="center" align="start">
                <n-grid cols="1 s:1 m:2 l:2 xl:2" responsive="screen" x-gap="30"
                        y-gap="20">
                    <n-grid-item>
                        <n-grid cols="1" responsive="screen" y-gap="10">
                            <n-grid-item>
                                <n-text tag="div"  style="font-size: 250%;font-weight: 100;">
                                    植物病害鉴定
                                </n-text>
                                <n-text code style="color: palevioletred;">Plant Disease Identification</n-text>
                            </n-grid-item>
                            <n-grid-item style="width: 100%">
                                <n-image src="src/assets/images/corn2.jpg"
                                         style="width: 100%;"
                                         class="sm:max-h-52 md:max-h-[15rem] xl:max-h-[10rem] 2xl:max-h-72"
                                         width="100%" object-fit="cover"></n-image>
                            </n-grid-item>
                            <n-grid-item>
                                <n-h2 style="font-weight: 100;" prefix="bar">植物病害诊断变得简单</n-h2>
                                <n-text style="font-weight: 100; font-size: 120%">
                                    <n-ellipsis expand-trigger="click" line-clamp="2" :tooltip="false">
                                        欢迎来到我们的植物病害识别网站！我们致力于帮助园艺爱好者、农民和业余爱好者轻松准确地诊断植物病害。
                                        我们的平台采用最先进的人工智能技术，让用户可以快速识别和了解常见的植物病害。通过我们友好的用户界面，
                                        您可以轻松上传植物图片并获得即时诊断，以及有效管理疾病的建议。加入我们的社区，让您的植物健康茁壮成长！
                                    </n-ellipsis>
                                </n-text>
                            </n-grid-item>
                        </n-grid>
                    </n-grid-item>

                    <n-grid-item>
                        <n-grid cols="1" responsive="screen">
                            <n-grid-item>
                                <n-image src="src/assets/images/corn3.jpg"
                                         style="width: 100%;"
                                         width="100%"
                                         class="sm:max-h-52 md:max-h-[15rem] xl:max-h-[10rem] 2xl:max-h-72"
                                         object-fit="cover"></n-image>
                            </n-grid-item>
                            <n-grid-item>
                                <n-h2 style="font-weight: 300" prefix="bar" type="info">基于计算机视觉与深度定制的模型技术
                                </n-h2>
                                <n-text>
                                    <n-ellipsis expand-trigger="click" line-clamp="5" :tooltip="false">
                                        利用计算机视觉和人工智能，结合神经网络识别和高精度模型检测玉米病虫害的技术，
                                        通过视频扫描技术和物联网无人机技术，实现了对大面积玉米田地进行快速、准确的监测和诊断。
                                        这项技术能够实现对玉米植株状况的实时监测、自动识别病虫害类型，并准确评估病虫害的严重程度，
                                        为农民提供及时的防治建议和精准农药施用方案。通过无人机技术，可以实现对田地的全方位覆盖，高效地获取图像数据，
                                        并与云端智能分析系统结合，实现玉米病虫害的早期预警和治理，进而提高农作物的产量和质量。这项技术整合了先进的信息技术和农业生产，
                                        为现代农业提供了一种智能化、高效化的解决方案，展现了数字化农业的巨大潜力。
                                    </n-ellipsis>

                                </n-text>
                            </n-grid-item>
                        </n-grid>


                    </n-grid-item>
                </n-grid>
            </n-space>
        </n-layout>
    </n-scrollbar>

  <!--    </n-space>-->


</template>

<script setup>


</script>

<style scoped lang="scss">
.scroll {
  overflow: auto;
}

/* 宽度、颜色和轨道背景 */
.scroll::-webkit-scrollbar {
  width: 4px; /* 滚动条宽度 */
}

.scroll::-webkit-scrollbar-track {
  background: transparent; /* 滚动条轨道背景颜色 */
}

/* 滚动条手柄 */
.scroll::-webkit-scrollbar-thumb {
  background-color: #bebebe; /* 滚动条手柄颜色 */
  border-radius: 6px; /* 滚动条手柄圆角 */
}

/* 鼠标悬停状态下的滚动条手柄 */
.scroll::-webkit-scrollbar-thumb:hover {
  background-color: #bebebe; /* 鼠标悬停时的手柄颜色 */
}

:deep(.n-space) {
  width: 100%;
  height: 100%;
}

:deep(.n-scrollbar) {
  width: 100%;

}

:deep(.n-scrollbar-container) {
  width: 100%;
  height: 100%;
}

:deep(.n-scrollbar-content) {
  width: 100%;
  height: 100%;
}

:deep(.n-layout) {
  width: 100%;
  //background-color: rebeccapurple;
}
</style>
