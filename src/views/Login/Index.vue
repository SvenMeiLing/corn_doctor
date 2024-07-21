<template>
    <canvas class="webgl"></canvas>
</template>

<script setup>
import {onMounted} from 'vue'
import * as Three from 'three'


onMounted(() => {
    // 定位画布
    const canvas = document.querySelector("canvas.webgl")
    console.log(canvas)
    // 场景
    const scene = new Three.Scene()
    // 几何图形
    const geometry = new Three.BoxGeometry(1, 1, 1)
    // 材质
    const material = new Three.MeshBasicMaterial({color: 0xff0000, wireframe: true})
    // 网格(放置图形和材质)
    const mesh = new Three.Mesh(geometry, material)
    scene.add(mesh)
    mesh.position.set(1, 2, 2)
    console.log(mesh.position.length())

    // 定义尺寸
    const sizes = {
        width: 800,
        height: 600
    }
    // 创建相机
    const camera = new Three.PerspectiveCamera(75, sizes.width / sizes.height)

    scene.add(camera)


    // 定义渲染位置
    const renderer = new Three.WebGLRenderer({
        canvas
    })

    // 设置画布大小
    renderer.setSize(sizes.width, sizes.height)
    renderer.render(scene, camera)
})

</script>

<style scoped>

</style>
