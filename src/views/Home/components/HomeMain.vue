<template>
  <!--Main内容入口-->
  <!--这里使用了 v-slot 指令和对象解构语法，将 Component 对象从 组件中解构出来。Component 是指当前路由所对应的组件。-->
    <router-view v-slot="{ Component }">
        <!--在 keep-alive中，使用 动态地渲染 Component 对象所表示的组件，并且给它设置一个唯一的 key 属性值 $route.path。如果该路由的 meta 标记了 keepAlive 属性，
        则显示这个组件。这样就可以使得这个组件被缓存下来，不会在每次切换路由时重新渲染。-->
        <keep-alive>
            <component :is="Component" :key="$route.path" v-if="$route.meta.keepAlive"/>
        </keep-alive>
        <component :is="Component" :key="$route.path" v-if="!$route.meta.keepAlive"/>
    </router-view>


</template>

<script setup>

</script>

<style lang="scss">
//.n-scrollbar-container {
//    height: 100%;
//}
//
//.n-scrollbar-content {
//    height: 100%;
//}

//.n-layout-content {
//    height: 100%;
//}
</style>
