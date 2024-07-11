/* 
    *global console
    *FileName:chatAI.js
    *PATH:src/apis
    *Time: 2024/7/8 11:34
    *Author: zzy
*/
import request from '@/utils/http.js'


export function chatAI(question) {
    return fetch(`${request.defaults.baseURL}/ai-chat`, {
        method: "POST",
        body: JSON.stringify({question: question}),
        headers: {
            'Content-Type': 'application/json' // 请求头，指定发送的数据类型为 JSON
            // 如果有其他请求头需要设置，可以在这里添加
        },
    });
}
