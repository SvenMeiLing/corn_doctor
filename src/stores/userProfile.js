/* 
    *global console
    *FileName:userProfile.js
    *PATH:src/stores
    *Time: 2024/5/27 20:57
    *Author: zzy
*/
import {reactive} from 'vue'
import {defineStore} from 'pinia'
import {loginAPI} from "@/apis/user.js";

export const useUserProfile = defineStore(
    'userProfile',
    () => {

        const profile = reactive({
            // 存储当前路由
            lastRoute: "home",
            // 存储用户上一次设置的菜单伸缩
            collapsed: false,
            // 登陆状态, 默认未登录
            isLoggedIn: false,
            // 存储jwt
            accessToken: null,
        })
        const userinfo = reactive({
            username: "匿名用户",
            location: "未知",
            avatar: "x.png",
            signature: "留下你的签名吧!",
            credit: 99
        })

        const setUserProfile = (key, value) => {
            profile[key] = value
        }
        const setUserinfo = (key, value) => {
            userinfo[key] = value
        }
        // 重置为默认配置
        const clearProfile = () => {
            profile.lastRoute = "home"
            profile.collapsed = false
            profile.isLoggedIn = false
            profile.accessToken = null
        }

        // 设置Token
        const getAccessToken = async () => {
            const {access_token} = await loginAPI()
            if (access_token) {
                profile.isLoggedIn = true
                profile.accessToken = access_token
            }

        }
        return {
            profile,
            userinfo,
            setUserinfo,
            setUserProfile,
            clearProfile,
            getAccessToken
        }
    },
    {
        persist: {
            storage: sessionStorage
        }
    }
)
