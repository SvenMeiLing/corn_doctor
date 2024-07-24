<template>
    <n-layout
            :native-scrollbar="false"
            class="p-[20px]"
            ref="containerRef"
    >
        <n-text>视频流式识别</n-text>
        <n-button @click="closeRAF">停止</n-button>
        <n-space>
            <video ref="videoEle" class="w-72 h-auto"
                   @loadedmetadata="videoLoaded"
                   autoplay
            ></video>
            <div ref="wrapCanvas" class="w-72 h-auto"></div>
        </n-space>

    </n-layout>
</template>

<script setup lang="ts">
import {onMounted, ref, nextTick} from 'vue'

const videoEle = ref<HTMLVideoElement | null>(null)
const wrapCanvas = ref<HTMLDivElement | null>(null)
const canvas = ref<HTMLCanvasElement | null>(null)
const context = ref<CanvasRenderingContext2D | null>(null)
const rafId = ref()
/**
 * 截屏
 */
const shot = () => {
    // 创建canvas
    canvas.value = document.createElement("canvas")
    canvas.value.width = videoEle.value.offsetWidth
    canvas.value.height = videoEle.value.offsetHeight
    //拿到 canvas 上下文对象
    context.value = canvas.value.getContext("2d");
    // 绘制图像
    context.value?.drawImage(videoEle.value, 0, 0, canvas.value.width, canvas.value.height)
    // 加入到指定容器中
    wrapCanvas.value.appendChild(canvas.value);//将 canvas 投到页面上
}

/**
 * 当video标签加载完成时调用初始截屏
 */
const videoLoaded = () => {
    shot()
}

// 使用 requestAnimationFrame 控制每秒绘制 60 次
let lastTime = 0;

function animate(currentTime) {
    const delta: Number = currentTime - lastTime;

    // 控制绘制的频率，每秒绘制 60 次
    if (delta > 1000 / 60) {
        context.value?.drawImage(videoEle.value, 0, 0, canvas.value.width, canvas.value.height);
        // console.log(canvas.value?.toDataURL('image/jpeg'))
        canvas.value?.toBlob((blob) => {
            // console.log(blob) 不断发起请求websocket
        }, "image/jpeg")
        lastTime = currentTime;
    }

    // 请求下一帧动画
    requestAnimationFrame(animate);
}

const closeRAF = () => {
    console.log("停止了", rafId.value)
    cancelAnimationFrame(rafId.value)
}
onMounted(async () => {

    // 开始动画循环

    rafId.value = requestAnimationFrame(animate);
    console.log(videoEle)
    let stream;
    try {
        stream = await navigator.mediaDevices.getUserMedia({video: true})
        videoEle.value.srcObject = stream;
    } catch (e) {
        console.log(e)
    }

})
// todo: 前端向服务端实时不断传输视频帧, 后端接收并不断返回视频帧, 前端每次接收一帧就播放一帧画面
</script>

<style scoped>

</style>
