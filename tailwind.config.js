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
}
