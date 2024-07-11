import {defineStore} from 'pinia'
import {ref} from 'vue'

export const useChatStore = defineStore(
    'chatStore',
    () => {

        // 存储消息
        const localChatHistory = ref([])
        // 设置消息列表
        const setLocalChatHistory = (value) => {
            localChatHistory.value = value
        }
        // 获取消息
        const getLocalChatHistory = () => {
            return localChatHistory.value
        }
        return {
            localChatHistory,
            setLocalChatHistory,
            getLocalChatHistory
        }
    },
    {
        persist: {
            paths: ["localChatHistory"]
        } // 默认持久化到localStorage, 遇到bug1:持久化有时候生效,忘记导入ref
    }
)
