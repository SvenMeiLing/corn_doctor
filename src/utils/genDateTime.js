/* 
    *global console
    *FileName:genDateTime.js
    *PATH:src/utils
    *Time: 2024/7/12 22:02
    *Author: zzy
*/
// 创建一个新的 Date 对象，表示当前时间
export const genDateTime = () => {
    let now = new Date();
    // 获取年、月、日、小时、分钟、秒
    let year = now.getFullYear(); // 年份，四位数字
    let month = now.getMonth() + 1; // 月份，注意 JavaScript 的月份是从 0 开始的，需要加 1
    let day = now.getDate(); // 获取日期
    let hours = now.getHours(); // 获取小时
    let minutes = now.getMinutes(); // 获取分钟
    let seconds = now.getSeconds(); // 获取秒数

    // 格式化月份、日期、小时、分钟、秒数为两位数
    month = month < 10 ? '0' + month : month;
    day = day < 10 ? '0' + day : day;
    hours = hours < 10 ? '0' + hours : hours;
    minutes = minutes < 10 ? '0' + minutes : minutes;
    seconds = seconds < 10 ? '0' + seconds : seconds;
    return `${year}/${month}/${day} ${hours}:${minutes}:${seconds}`;
}
