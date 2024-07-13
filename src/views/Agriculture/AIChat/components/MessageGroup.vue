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
                       @click="changeChecked(item.uuid)"
                       class="ms-1"
                >
                    <n-ellipsis class="max-w-24" v-if="item?.data?.length">
                        {{ item.data[0].text }}
                    </n-ellipsis>
                    <n-ellipsis class="max-w-24" v-else>
                        {{ index}}
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


const fakeMsgGroup = ref([])
const emit = defineEmits(['chatHistory'])


function sendCHToParent() {
    emit('chatHistory', fakeMsgGroup)
}

const myIndexedDB = localforage.createInstance({name: 'cornIndexedDB',})

const changeChecked = async (uuid) => {
    // 本来是{{data:[]}, {data:[]}}, 结果变成了[{data:[]}]
    // 把列表所有值变成false后再把当前索引变成true
    const newMsgGroup = fakeMsgGroup.value.map(group => {
        if (group.uuid === uuid) {
            console.log(group.uuid, "<---->", uuid)
            return {...group, lastSession: true, data: toRaw(group.data)}
        }
        return {...group, lastSession: false, data: toRaw(group.data)}
    })
    console.log(newMsgGroup, "<---newMsgGroup")
    fakeMsgGroup.value = newMsgGroup  // 向数组中添加一个消息组
    // 设置一个最后一次会话的索引值
    await myIndexedDB.setItem("chatHistory", toRaw(fakeMsgGroup.value))
    sendCHToParent()

}

async function addSession() {
    // 添加一个消息组到indexedDB, 也加入到消息组变量中
    const oneMsgGroup = {
        uuid: uuid4(),
        data: [],
        lastSession: true,
    }
    fakeMsgGroup.value.unshift(oneMsgGroup)
    console.log(toRaw(fakeMsgGroup.value), "<---插入后的数组")
    // 设置一个最后一次会话的索引值
    await myIndexedDB.setItem("chatHistory", toRaw(fakeMsgGroup.value))
    // 设置高亮为当前创建的会话
    await changeChecked(oneMsgGroup.uuid)
}


onMounted(async () => {
    // 先获取一次indexedDB中的数据
    const chatHistory = await myIndexedDB.getItem('chatHistory');
    if (!chatHistory) {
        // 如果没有历史消息记录就新建一个tag
        await addSession()
        console.log('已新建')
    }
    // 新建完成后再次获取最新的值
    const newChatHistory = await myIndexedDB.getItem('chatHistory');
    fakeMsgGroup.value = newChatHistory
    console.log(newChatHistory, "<---newChatHistory")
    console.log(fakeMsgGroup.value, "<---fakeMsgGroup")
    // 传递值给父组件
    sendCHToParent()
})
</script>

<style scoped>
:deep(.n-menu-item-content-header) {
    border: 1px solid red;
    border-radius: 7px;
}
</style>
