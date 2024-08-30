/* 
    *global console
    *FileName:login.js
    *PATH:src/apis
    *Time: 2024/8/29 22:55
    *Author: zzy
*/
import request from '@/utils/http.js'

export const loginAPI = (username = "zzym", password = "168168956") => {
    return request({
        url: 'login/access-token',
        method: 'POST',
        data: {
            username,
            password
        },
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',  // 或 'application/x-www-form-urlencoded'
        },
    })
}

export const logoutAPI = () => {
    return request("/logout")
}
