/* 
    *global console
    *FileName:index.js
    *PATH:src/router
    *Time: 2024/5/23 17:12
    *Author: zzy
*/
// createRoute: 创建route实例对象
// createHistory: 创建history模式路由
import {createRouter, createWebHistory} from 'vue-router'

import Layout from '@/views/Layout/Index.vue'
// import NotFound from '@/views/Error/404.vue'
import NProgress from "nprogress";
import "nprogress/nprogress.css";
import {useUserProfile} from "@/stores/userProfile.js";
import {validateJwtFormat} from '@/utils/useValidJWT.js'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        // path和components对应关系的未知
        {
            path: "/",
            component: Layout,
            children: [
                {
                    path: "",
                    component: () => import('@/views/Home/components/HomeSummary.vue'), // 主页,
                    meta: {title: '玉米医生', requireAuth: false}
                },
                {
                    path: "/recognition",
                    component: () => import('@/views/Recognition/Index.vue'), //
                    meta: {title: '病害识别', keepAlive: true}
                },
                {
                    path: "/agriculture",
                    // component: () => import('@/views/agriculture/Index2.vue'),
                    children: [
                        {
                            path: "disease",
                            component: () => import('@/views/Agriculture/Disease/Index.vue'),
                            meta: {
                                title: "病害百科", keepAlive: true
                            }
                        },
                        {
                            path: "store",
                            component: () => import('@/views/Agriculture/Store/Index.vue'),
                            meta: {title: "农业商城", keepAlive: true}
                        },
                        {
                            path: "ai-chat",
                            component: () => import('@/views/Agriculture/AIChat/Index.vue'),
                            meta: {title: "AI服务"}
                        },
                        {
                            path: "visualization",
                            component: () => import('@/views/Agriculture/DiseaseVisual/Index.vue'),
                            meta: {title: "数据展板"}
                        }
                    ]
                },
                {
                    path: "/page5",
                    component: () => import('@/views/Page5/Index.vue'),
                    meta: {title: "日记簿"}
                },
                {
                    path: "/flow-recognition",
                    component: () => import('@/views/flow-recognition/Index.vue'),
                    meta: {title: "流式识别"}
                },
                {
                    path: "/login",
                    component: () => import('@/views/Login/Index.vue'),
                    meta: {title: "登录", requireAuth: false},
                    name: "login",
                },
                {
                    path: "/community",
                    component: () => import('@/views/Community/Index.vue'),
                    meta: {title: "社区"},
                    name: "community",
                },
                // ---------------匹配404---------------
                {
                    path: "/:catchAll(.*)",
                    redirect: "/404"
                },
                {
                    path: "/404",
                    component: import("@/views/Error/404.vue"),
                    meta: {title: "404"},
                    name: "404"
                }
            ]
        },
    ],
    // 路由滚动行为定制(路由切换时, 自动滚到顶部)
    scrollBehavior() {
        return {
            top: 0
        }
    }
})

export function setupRouterGuard(router) {
    createProgressGuard(router);
}


export function createProgressGuard(router) {
    router.beforeEach(async () => {
        // 执行进度条
        NProgress.start();
        return true;
    });
    router.afterEach(async () => {
        // 结束进度条
        NProgress.done();
        return true;
    });
}

NProgress.configure({

    easing: 'ease', // 动画方式

    speed: 500, // 递增进度条的速度

    showSpinner: false, // 是否显示加载 icon

    trickleSpeed: 200, // 自动递增间隔

    minimum: 0.3 // 初始化时的最小百分比

})

export function createShowTitle(router) {
    router.beforeEach((to, from, next) => {
        // 如果跳转的路由地址有title属性,则需要更改浏览器标签页title
        if (to.meta.title) document.title = to.meta.title
        // 跳转指定路由
        next()
    })
}

export function loginRedirect(router) {
    const userProfile = useUserProfile()
    router.beforeEach((to, from, next) => {
        // 如果已经登录,依然访问login视图, 则跳转到home
        if (userProfile.profile.isLoggedIn && to?.name?.includes("login")) {
            console.log("包含")
            next("/")
        } else {
            next()
        }
    })
}

/*
校验路由是否可以访问
 */
export function requireAuth(router) {
    router.beforeEach((to, from, next) => {
        // 如果当前访问的路由需要验证, 且处于未登陆状态
        const userProfile = useUserProfile()
        // todo: 如果当前页需要认证,交由下一逻辑处理
        if (to.meta.requireAuth !== false) {
            let token = userProfile.profile.accessToken
            if (token && validateJwtFormat(token)) {
                // 对token的基本校验, 防止随便伪造token
                next()
            } else {
                // token无效, 清除token和登陆状态
                userProfile.setUserProfile("accessToken", null)
                userProfile.setUserProfile("isLoggedIn", false)
                window.$message?.error("已清除无效的令牌Token,请重新登录!")
                next("/login")
            }
        } else {
            // 不需要校验的页面, 直接放行
            next()
        }
    })
}

export default router
