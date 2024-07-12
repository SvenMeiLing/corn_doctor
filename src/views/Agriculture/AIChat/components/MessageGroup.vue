<template>
    <n-flex align="center" :wrap="false" class="w-1/2">
        <n-text tag="b">历史会话:</n-text>

        <n-flex class="w-5/6 h-7" :wrap="false">
            <n-scrollbar>
                <!--系统预制-->
                <n-tag
                        type="primary"
                        class="me-2 cursor-pointer"
                        @click="addSession"
                        :bordered="false"
                >
                    <n-ellipsis class="w-auto">
                        + 新增会话
                    </n-ellipsis>
                </n-tag>
                <!--浏览器存储的每条消息记录-->
                <n-tag v-for="(item, index) in fakeMsgGroup"
                       :key="index"
                       type="primary"
                       checkable
                       bordered
                       v-model:checked="item.lastSession"
                       @click="changeChecked(item)"
                >
                    <n-ellipsis class="w-24">
                        {{ item.data[0].text }}
                    </n-ellipsis>
                </n-tag>
            </n-scrollbar>
        </n-flex>
    </n-flex>

</template>

<script setup>
import {ref, onMounted, toRaw} from "vue";
import {defineEmits} from 'vue'
import localforage from "localforage";
import {v4 as uuid4} from 'uuid'
import {genDateTime} from "@/utils/genDateTime.js";

const emit = defineEmits(['chatHistory'])
const fakeMsgGroup = ref([])

function sendCHToParent() {
    emit('chatHistory', fakeMsgGroup)
}

const myIndexedDB = localforage.createInstance({name: 'cornIndexedDB',})

async function addSession() {
    // 添加一个消息组到indexedDB, 也加入到
    const oneMsgGroup = {
        uuid: uuid4(),
        data: [
            {
                dateTime: genDateTime(),
                text: "这是一个新的会话"
            }
        ],
        lastSession: true,

    }
    fakeMsgGroup.value.unshift(oneMsgGroup)
    console.log(toRaw(fakeMsgGroup))
    // 设置一个最后一次会话的索引值
    await myIndexedDB.setItem("chatHistory", toRaw(fakeMsgGroup))
    await changeChecked(oneMsgGroup)
}


const changeChecked = async (item) => {
    // 把列表所有值变成false后再把当前索引变成true
    const newMsgGroup = fakeMsgGroup.value.map(value => {
        if (value === item) {
            return {...value, lastSession: true, data: toRaw(value.data)}
        }
        return {...value, lastSession: false, data: toRaw(value.data)}
    })
    fakeMsgGroup.value = newMsgGroup
    // 设置一个最后一次会话的索引值
    await myIndexedDB.setItem("chatHistory", newMsgGroup)
    sendCHToParent()

}
onMounted(async () => {
    const myIndexedDB = localforage.createInstance({name: 'cornIndexedDB',})
    const chatHistory = await myIndexedDB.getItem('chatHistory');
    fakeMsgGroup.value = chatHistory
    sendCHToParent()
})
</script>

<style scoped>
:deep(.n-menu-item-content-header) {
    border: 1px solid red;
    border-radius: 7px;
}
</style>
