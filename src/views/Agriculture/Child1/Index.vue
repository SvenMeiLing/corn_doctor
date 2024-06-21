<template>
    <div>
        <TransitionGroup>
            <div v-for="item in list" :key="item.id">
                {{item.number}}
            </div>
        </TransitionGroup>
    </div>
</template>
<script setup lang="ts">
import {ref} from 'vue'

let list = ref(Array.apply(null, {length: 81} as number[]).map((_, index) => {
        return {
            id: index,
            number: (index % 9)
        }
    }
))
console.log(list)
</script>
