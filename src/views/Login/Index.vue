<template>
    <canvas class="webgl"></canvas>
</template>

<script setup>
import * as Three from 'three'

const scene = new Three.Scene()
const geometry = new Three.BoxGeometry(1, 1, 1)
const material = new Three.MeshBasicMaterial({color: 0xff0000})
const mesh = new Three.Mesh(g)
</script>

<style scoped>

</style>
