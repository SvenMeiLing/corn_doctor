/* 
    *global console
    *FileName:userProfile.js
    *PATH:src/stores
    *Time: 2024/5/27 20:57
    *Author: zzy
*/
import {reactive} from 'vue'
import {defineStore} from 'pinia'

export const useUserProfile = defineStore(
    'userProfile',
    () => {


        const profile = reactive({
            // 存储当前路由
            lastRoute: "home",
            // 存储用户上一次设置的菜单伸缩
            collapsed: false,
            // 登陆状态, 默认未登录
            isLoggedIn: true
        })

        const setUserProfile = (key, value) => {
            profile[key] = value
        }
        return {
            profile,
            setUserProfile
        }
    },
    {
        persist: {
            storage: sessionStorage
        }
    }
)
