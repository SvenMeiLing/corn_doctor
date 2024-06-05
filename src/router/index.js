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
import NProgress from "nprogress";
import "nprogress/nprogress.css";

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
                    meta: {title: '玉米医生'}
                },
                {
                    path: "/recognition",
                    component: () => import('@/views/Recognition/Index.vue'), //
                    meta: {title: '病害识别'}
                },
                {
                    path: "/page3",
                    component: () => import('@/views/Page3/Index.vue'),
                    children: [
                        {
                            path: "child1",
                            component: () => import('@/views/Page3/Child1/Index.vue')
                        },
                        {
                            path: "child2",
                            component: () => import('@/views/Page3/Child2/Index.vue')
                        },
                        {
                            path: "child3",
                            component: () => import('@/views/Page3/Child3/Index.vue')
                        },
                    ]
                }
            ]
        }
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

export default router
