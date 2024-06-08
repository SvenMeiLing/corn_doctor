/* 
    *global console
    *FileName:upload.js
    *PATH:mock
    *Time: 2024/6/7 19:33
    *Author: zzy
*/
// 导入 Mock.js
import Mock from 'mockjs';

// 设置 Mock.js 的拦截规则
Mock.mock('http://127.0.0.1:3000/upload', 'post', function (options) {

    // 获取上传的文件数据 -> [{name:'1.jpg',file:File}, ...]
    const formData = options.body;
    let responseData = []
    // 返回模拟的响应数据
    formData.forEach(fileObj => {
        console.log(Object.keys(fileObj),"====",Object.values(fileObj))
        responseData.push(
            {
                fileName: fileObj.name,
                fileSize: fileObj.size
            }
        )
    });
    console.log(responseData)
    return Mock.mock({
        code: 200,
        message: 'Files uploaded successfully',
        data: responseData
    });
});
