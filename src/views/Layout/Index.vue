<template>
    <n-layout class="layout">
        <LayoutHeader class="header"></LayoutHeader>
        <n-layout has-sider class="main">
            <Home></Home>
        </n-layout>
        <LayoutFooter class="footer"></LayoutFooter>
    </n-layout>


</template>

<style scoped lang="scss">
.layout {
  height: 100%;
  display: flex;

  width: 100%;

  .header {
    flex: 1 0 0;
  }

  .main {
    flex: 7 0 0;

  }

  .footer {
    flex: 1 0 0;

  }
}


</style>
<script setup>
import LayoutHeader from "@/views/Layout/components/LayoutHeader.vue";
import Home from "@/views/Home/Index.vue"
import LayoutFooter from "@/views/Layout/components/LayoutFooter.vue";
import {useMessage, useLoadingBar} from 'naive-ui'

window.$message = useMessage()
</script>
