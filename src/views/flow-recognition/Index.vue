<template>
    <n-layout
            :native-scrollbar="true"
            class="p-[20px]"
    >
        <n-text>视频流式识别</n-text>
        <video ref="videoEle" class="w-72 h-60"></video>
    </n-layout>
</template>

<script setup>
import {onMounted, ref} from 'vue'

const videoEle = ref(null)

const shot = () => {
    const canvas = document.createElement("canvas")
    canvas.width = videoEle.value.width
    canvas.height = videoEle.value.height
}
onMounted(async () => {
    console.log(videoEle)
    let stream;
    try {
        stream = await navigator.mediaDevices.getUserMedia({video: true})
        videoEle.value.srcObject = stream;
        videoEle.value.play()
    } catch (e) {
        console.log(e)
    }

})
// todo: 前端向服务端实时不断传输视频帧, 后端接收并不断返回视频帧, 前端每次接收一帧就播放一帧画面
</script>

<style scoped>

</style>
