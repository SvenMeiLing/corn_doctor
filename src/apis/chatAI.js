/* 
    *global console
    *FileName:chatAI.js
    *PATH:src/apis
    *Time: 2024/7/8 11:34
    *Author: zzy
*/
import request from '@/utils/http.js'

export function getAIAnswer(data) {
    return request('/ai-chat', {
        method: "POST",
        responseType: 'stream',  // 响应类型设置为流
        data,
    })
}
