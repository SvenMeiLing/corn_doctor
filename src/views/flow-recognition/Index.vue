<template>
    <n-layout
            :native-scrollbar="false"
            class="p-[20px]"
            ref="containerRef"
    >
        <n-text tag="div" class="text-2xl">这是一个实验性功能,你可以先试试试试!🧐</n-text>
        <n-space class="mt-2">
            <n-button @click="flowRecognition" type="primary">开始</n-button>
            <n-button @click="socket.close()" type="error">停止</n-button>
        </n-space>

        <hr>
        <div class="w-64 h-48 rounded-md dark:bg-zinc-800 bg-zinc-200 flex items-center justify-center"
        >
            <!--展示摄像头画面-->
            <img ref="imgRef" class="rounded-md" v-show="isShow" id="output" width="240" height="180" alt="from camera">
            <!--占位符-->
            <CameraAction class="w-32" v-show="!isShow"/>

        </div>
        <video ref="videoRef" id="video" class="hidden" width="240" height="180" autoplay></video>
    </n-layout>
</template>

<script setup lang="ts">
import {onMounted, ref} from 'vue'
import {CameraAction} from '@vicons/carbon'

const isShow = ref<Boolean>(false)
const videoRef = ref<HTMLVideoElement | null>(null)
const imgRef = ref<HTMLImageElement | null>(null)
let socket: WebSocket;
let stream: MediaStream;

/*
开启ws连接
 */
const startWebSocket = () => {
    socket = new WebSocket("ws://127.0.0.1:8000/ws");
    socket.onopen = () => {
        console.log("WebSocket connection established");
        const canvas = document.createElement('canvas');
        const ctx = canvas.getContext('2d');
        canvas.width = videoRef.value.width;
        canvas.height = videoRef.value.height;
        const timeId = setInterval(() => {
            // 间隔100ms 发送一帧摄像机画面给后端
            ctx?.drawImage(videoRef.value, 0, 0, canvas.width, canvas.height);
            const frame = canvas.toDataURL('image/jpeg');
            if (socket.readyState === socket.OPEN) {
                socket.send(frame);
            } else if (socket.readyState === socket.CLOSED) {
                // 当链接关闭,停止向后端发送帧, 并关闭摄像头, 同时屏蔽画面
                clearInterval(timeId)
                if (stream) {
                    // 遍历所有的轨道，停止每一个视频轨道
                    stream.getTracks().forEach(track => {
                        if (track.kind === 'video') {
                            track.stop();
                        }
                    });
                }
                isShow.value = false
                console.log("连接已经关闭");
            }
        }, 100); // 每 100 毫秒发送一帧
    };

    socket.onmessage = (event) => {
        console.log("收到了图像帧")
        isShow.value = true
        console.log(imgRef.value)
        imgRef.value.src = event.data;

    };

    socket.onclose = () => {
        console.log("WebSocket connection closed");
    };

    socket.onerror = (error) => {
        console.error("WebSocket error: ", error);
    };
}

/*
获取用户摄像头视频流
 */
const getMediaStream = async () => {
    // 获取摄像头视频流
    try {
        stream = await navigator.mediaDevices.getUserMedia({
            video: {
                facingMode: {exact: "user"}
            }
        })
        videoRef.value.srcObject = stream;
        await videoRef.value.play();
    } catch (err) {
        console.log(err)
    }
}

/*
调用方法进行流式识别
 */
const flowRecognition = async () => {
    // 获取摄像头并建立ws链接
    await getMediaStream()
    startWebSocket()
}
</script>

<style scoped>

</style>
