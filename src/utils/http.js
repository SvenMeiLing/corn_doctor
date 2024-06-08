/* 
    *global console
    *FileName:http.js
    *PATH:src/utils
    *Time: 2024/6/7 19:39
    *Author: zzy
*/
import axios from 'axios'

export const httpInstance = axios.create({
    baseURL: "http://127.0.0.1:3000",
    timeout: 2500,
})
// axios响应式拦截器
httpInstance.interceptors.response.use(res => res.data,
    e => {
        // 统一错误提示
        window.$message.warning(e.message)
        return e
    })

export default httpInstance
