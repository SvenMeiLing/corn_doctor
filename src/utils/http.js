/* 
    *global console
    *FileName:http.js
    *PATH:src/utils
    *Time: 2024/6/7 19:39
    *Author: zzy
*/
import axios from 'axios'
import NProgress from "nprogress";
import codeMessage from "@/utils/codeMessage.js";
import {useUserProfile} from "@/stores/userProfile.js";
import {useRouter} from "vue-router";

// 过滤掉一些不需要progress的路由
const noProgress = ["ranking"]

const router = useRouter()

NProgress.configure({

    easing: 'ease', // 动画方式

    speed: 500, // 递增进度条的速度

    showSpinner: false, // 是否显示加载 icon

    trickleSpeed: 300, // 自动递增间隔

    minimum: 0.3 // 初始化时的最小百分比

})
export const httpInstance = axios.create({
    baseURL: "http://127.0.0.1:8000/api/v1",
    timeout: 45000,
})


// axios请求拦截器
httpInstance.interceptors.request.use(
    config => {
        // 获取用户数据
        const userProfile = useUserProfile()
        // 拼接token
        const token = userProfile.profile.accessToken
        if (token) {
            config.headers.Authorization = `Bearer ${token}`
        }
        // 移除某些不需要进度条动画的路由
        if (!noProgress.includes(config.url.split("/").pop())) {
            NProgress.start(); // 显示进度条
        }
        return config;
    }, error => {
        NProgress.done(); // 隐藏进度条
        return Promise.reject(error);
    }
);


// axios响应式拦截器
httpInstance.interceptors.response.use(res => {
        NProgress.done(); // 隐藏进度条
        return res.data
    },
    e => {
        NProgress.done(); // 隐藏进度条
        // 统一错误提示
        if (!e.response) {
            // 如果没有响应则代表本地网络错误
            window.$message.warning("网络出现错误!")
            return e
        }
        if (e.response.status !== 200) {
            // 发送预制错误信息
            window.$message.warning(codeMessage[e.response.status])
        } else if (e.response.status === 401) {
            console.log(401)
            // token失效,清楚本地消息
            const userProfile = useUserProfile()
            // 清楚信息
            userProfile.clearProfile()
            // 跳转到/login
            router.push("/login")
        }
        return e
    })

export default httpInstance
