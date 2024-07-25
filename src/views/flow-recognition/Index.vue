<template>
    <n-layout
            :native-scrollbar="false"
            class="p-[20px]"
            ref="containerRef"
    >
        <n-text>视频流式识别</n-text>
        <n-button @click="switchRAF">停止</n-button>
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
    rafId.value = requestAnimationFrame(animate);
}

// 使用 requestAnimationFrame 控制每秒绘制 60 次
let lastTime = 0;
// 现在目前问题是如何使其发送消息给后端
const ws = ref<WebSocket>(new WebSocket("ws://localhost:8000/ws"))
console.log("监听中...", ws.value)
ws.value.onopen = function () {
    console.log("建立了一个链接")
    ws.value.send(new Blob())
}

ws.value.onmessage = function (ev) {
    console.log(ev.data, "<---接收到消息")
}

function animate(currentTime) {
    const delta: Number = currentTime - lastTime;

    // 控制绘制的频率，每秒绘制 60 次
    if (delta > 1000 / 60) {
        context.value?.drawImage(videoEle.value, 0, 0, canvas.value.width, canvas.value.height);
        // xyxy 数据（假设从后端获取到的）
        const boxes = [
            [213.33, 231.95, 439.68, 325.68],
            [0.0821, 4.3731, 65.067, 84.469],
            [96.574, 394.24, 360.03, 509.88],
            [9.9315, 321.58, 158.29, 405.19]
        ];

        // 设置绘制矩形框的样式
        context.value.strokeStyle = 'green';
        context.value.lineWidth = 2;

        // 遍历并绘制所有的框
        boxes.forEach(box => {
            const [x_min, y_min, x_max, y_max] = box;
            const width = x_max - x_min;
            const height = y_max - y_min;
            context.value?.strokeRect(x_min, y_min, width, height);
            // // 绘制标签
            context.value.font = '16px Arial';
            context.value.fillStyle = 'red';
            context.value.fillText("xxx", x_min, y_min); // 在框上方显示标签
        });


        // console.log(canvas.value?.toDataURL('image/jpeg'))
        canvas.value?.toBlob((blob) => {
            // console.log(blob) 不断发起请求websocket
            ws.value.send(blob)
        }, "image/jpeg")
        lastTime = currentTime;
    }

    // 请求下一帧动画
    rafId.value = requestAnimationFrame(animate);
}

const paused = ref(false)
const switchRAF = () => {
    if (paused.value) {
        rafId.value = requestAnimationFrame(animate);
        paused.value = false
    } else {
        console.log("停止了", rafId.value)
        paused.value = true
        cancelAnimationFrame(rafId.value)
    }

}
onMounted(async () => {

    // 开始动画循环

    // rafId.value = requestAnimationFrame(animate);

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
