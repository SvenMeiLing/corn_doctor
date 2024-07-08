/* 
    *global console
    *FileName:testAPI.js
    *PATH:src/apis
    *Time: 2024/7/8 22:53
    *Author: zzy
*/

import axios from "axios";

axios({
    method: 'post',
    url: 'http://127.0.0.1:8000/api/v1/ai-chat', // 替换为你的流式接口URL
    responseType: 'stream',
    data: {question: "请告诉我玉米叶枯病的治疗方式和防治手段并提出多条有效建议"}
})
    .then(response => {
        // 这里的response.data是一个Node.js的流（Stream）对象
        response.data.on("data", (chunk) => {
            console.log(chunk.toString());
            // 处理每个数据块，例如写入文件或进行其他操作
        });

        response.data.on("end", (end) => {
            console.log(end, "end")
            // 数据接收完毕的处理逻辑
        })
    })
