<template>
    <n-layout
            :native-scrollbar="false"
            class="p-[20px]"
            ref="containerRef"
            id="visualContainer"
            content-class="w-full h-full flex flex-wrap sm:flex-nowrap gap-2"
    >
        <n-tabs type="line" animated class="w-1/2">
            <n-tab-pane name="login" tab="登录/Login" display-directive="show:lazy">
                <SignIn></SignIn>
            </n-tab-pane>
            <n-tab-pane name="register" tab="注册/Register" display-directive="show:lazy" disabled>
                <Register></Register>
            </n-tab-pane>
        </n-tabs>


    </n-layout>
</template>

<script setup>

import Register from "@/views/Login/components/Register.vue";
import SignIn from "@/views/Login/components/SignIn.vue";
</script>

<style scoped>

</style>
