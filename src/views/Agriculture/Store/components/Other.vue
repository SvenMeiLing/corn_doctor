<template>
  <!-- 第三部分 -->
    <n-flex vertical class=" w-full md:w-1/2 xl:w-1/3">
        <n-card size="small">
            <template #header>
                新品速推
            </template>
            <template #default>
                <n-list hoverable clickable>
                    <n-list-item>
                        <n-thing title="代森锰锌" content-style="margin-top: 10px;">
                            <template #description>
                                <n-space size="small" style="margin-top: 4px">
                                    <n-tag :bordered="false" type="info" size="small">
                                        进口
                                    </n-tag>
                                    <n-tag :bordered="false" type="info" size="small">
                                        联合研发
                                    </n-tag>
                                </n-space>
                            </template>
                            <template #default>
                                <n-image src="/">

                                </n-image>
                            </template>
                        </n-thing>
                    </n-list-item>
                </n-list>
            </template>
        </n-card>
    </n-flex>
</template>

<script setup>
import DJI from '@/components/DJI.vue'
import iFlytek from '@/components/iFlytek.vue'
</script>

<style scoped>

</style>
