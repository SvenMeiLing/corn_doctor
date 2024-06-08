/* 
    *global console
    *FileName:recognition.js
    *PATH:src/apis
    *Time: 2024/6/7 21:34
    *Author: zzy
*/
import request from '@/utils/http.js'
import axios from "axios";

export function uploadImg(data) {
    return request.post("/upload", data, {
        onUploadProgress: function (e) {
            console.log('Upload progress:', e);
        }
    });
}
