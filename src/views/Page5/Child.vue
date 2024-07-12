<template>
    <ul>
        <li v-if="list" v-for="item in props.list">{{item}}</li>
    </ul>
</template>

<script setup>
const props = defineProps({
    list: {
        type: Array,
        default: []
    }
})
</script>

<style scoped>

</style>
