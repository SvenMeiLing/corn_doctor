/* 
    *global console
    *FileName:useValidJWT.js
    *PATH:src/utils
    *Time: 2024/8/29 14:19
    *Author: zzy
*/
function isBase64Url(str) {
    // Base64Url 字符串应只包含字母、数字、-、_ 和 Base64 末尾的 =（可选）
    const base64UrlPattern = /^[A-Za-z0-9-_]+={0,2}$/;
    return base64UrlPattern.test(str);
}

export function validateJwtFormat(token) {
    // 去除 `Bearer ` 前缀
    const jwt = token?.startsWith('Bearer ') ? token?.slice(7) : token;

    // 分割 JWT
    const parts = jwt?.split('.');

    // 确保有三个部分
    if (parts?.length !== 3) {
        return false;
    }

    // 检查每一部分是否符合 Base64Url 编码规则
    return parts?.every(isBase64Url);
}
