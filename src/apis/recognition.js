/* 
    *global console
    *FileName:recognition.js
    *PATH:src/apis
    *Time: 2024/6/7 21:34
    *Author: zzy
*/
import request from '@/utils/http.js'

export function uploadImg(data) {
    return request('/plant/yolo_identify', {
        method: "POST",
        data
    })
}
