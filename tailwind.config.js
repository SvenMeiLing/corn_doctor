/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
        "./src/**/*.{html,js,vue}" // 加入这个不然vue文件不生效
    ],
    theme: {
        extend: {},
    },
    plugins: [],
    darkMode: ['selector', '#dark'], // 找到黑暗模式的标签, 可dark:bg-red-400 适配黑暗模式
    important: true, // 强制样式
}
