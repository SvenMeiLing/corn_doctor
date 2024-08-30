/* 
    *global console
    *FileName:useDefer.js
    *PATH:src/utils
    *Time: 2024/8/29 13:05
    *Author: zzy
*/
import {ref, onUnmounted} from 'vue';

export function useDefer(maxCount = 100) {
    const frameCount = ref(0);
    let rafId;

    function updateFrameCount() {
        rafId = requestAnimationFrame(() => {
            frameCount.value++;
            if (frameCount.value >= maxCount) {
                return;
            }
            updateFrameCount()
        })
    }

    updateFrameCount()
    onUnmounted(() => {
        cancelAnimationFrame(rafId)
    })
    return function defer(n) {
        return frameCount.value >= n;
    }
}
