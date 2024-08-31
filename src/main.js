import './assets/main.css'
import "/mock"
import {createApp} from 'vue'
import App from './App.vue'
import naive from 'naive-ui'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import {createShowTitle, loginRedirect, requireAuth, setupRouterGuard} from './router/index.js'
import router from './router'
import "@/apis/recognition.js"
// 通用字体
import 'vfonts/Lato.css'
// 等宽字体
import 'vfonts/FiraCode.css'
//1.导入createPinia
import {createPinia} from "pinia"


//2.执行方法得到示例
const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)
const app = createApp(App).use(router)

app.use(pinia)
    .use(naive)
    .mount('#app')

// 已登录用户重定向行为
loginRedirect(router)
// 校验路由通过
requireAuth(router)
// 路由进度条,请求进度条
setupRouterGuard(router);
// 标签页title更新
createShowTitle(router)

