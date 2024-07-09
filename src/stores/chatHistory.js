import {defineStore} from 'pinia'

export const useChatStore = defineStore(
    'chatStore',
    () => {


        const localChatHistory = ref([])
        const setLocalChatHistory = (value) => {
            localChatHistory.value = value
        }
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
            storage: localStorage,
            paths: ["localChatHistory"]
        }
    }
)
