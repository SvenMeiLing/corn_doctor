/* 
    *global console
    *FileName:recognition.js
    *PATH:src/apis
    *Time: 2024/6/7 21:34
    *Author: zzy
*/
import request from '@/utils/http.js'

export function uploadImg(data) {
    return request.post("http://127.0.0.1:8000/upload", data, {
        onUploadProgress: function (e) {
            console.log('Upload progress:', e);
        },
    });
}
