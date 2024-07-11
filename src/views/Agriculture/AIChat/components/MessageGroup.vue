<template>
    <n-flex align="center" :wrap="false" class="w-1/2">
        <n-text tag="b" class="w-max">历史会话:</n-text>
        <n-flex class="w-5/6 " :wrap="false">
            <n-tag v-for="(item, index) in fakeMsgGroup"
                   :key="index"
                   class="focus:bg-red-300 button"
                   checkable
                   bordered
                   v-model:checked="checkList[index]"
                   @click="changeChecked"

            >
                <n-ellipsis class="w-14">
                    {{ item.data[0].text }}
                </n-ellipsis>
            </n-tag>
        </n-flex>


    </n-flex>

</template>

<script setup>
import {ref, onMounted} from "vue";
import {NIcon, useMessage} from "naive-ui";

import localforage from "localforage";

const fakeMsgGroup = ref([])
const checkList = ref([])
const checked = ref(false)
const changeChecked = () => {
    // 拿到某个关键值, 给当前点击的tag加上checked=true
    console.log(checkList.value)
}
const handleUpdateValue = (key, item) => {

}
onMounted(async () => {
    const myIndexedDB = localforage.createInstance({name: 'cornIndexedDB',})
    const chatHistory = await myIndexedDB.getItem('chatHistory');
    fakeMsgGroup.value = chatHistory
    console.log(Array().fill(false, 0, fakeMsgGroup.value.length))
    checkList.value = new Array(fakeMsgGroup.value.length).fill(false)
})
</script>

<style scoped>
:deep(.n-menu-item-content-header) {
    border: 1px solid red;
    border-radius: 7px;
}
</style>
