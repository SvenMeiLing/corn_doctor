import './assets/main.css'
import "/mock"
import {createApp} from 'vue'
import App from './App.vue'
import naive from 'naive-ui'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import {createShowTitle, setupRouterGuard} from './router/index.js'
import router from './router'
import "@/apis/recognition.js"
// 通用字体
import 'vfonts/Lato.css'
// 等宽字体
import 'vfonts/FiraCode.css'


//1.导入createPinia
import {createPinia} from "pinia"

// 路由进度条,请求进度条
setupRouterGuard(router);
// 标签页title更新
createShowTitle(router)
//2.执行方法得到示例
const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)
createApp(App)
    .use(router)
    .use(pinia)
    .use(naive)
    .mount('#app')
