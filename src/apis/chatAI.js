/* 
    *global console
    *FileName:chatAI.js
    *PATH:src/apis
    *Time: 2024/7/8 11:34
    *Author: zzy
*/
import request from '@/utils/http.js'
import axios from "axios";

export function getAIAnswer(data) {
    return request('/ai-chat', {
        method: "POST",
        responseType: 'stream',  // 响应类型设置为流
        data,
    })
}

export function getStreamAIAnswer(data) {
    return axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/api/v1/ai-chat', // 替换为你的流式接口URL
        responseType: 'stream',
        data: data
    });
}
