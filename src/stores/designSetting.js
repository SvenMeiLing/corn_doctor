/* 
    *global console
    *FileName:designSetting.js
    *PATH:src/views/stores
    *Time: 2024/5/23 21:57
    *Author: zzy
*/
import {ref, computed} from 'vue'
import {defineStore} from "pinia"
import {darkTheme} from 'naive-ui'
import {LightbulbOutlined, DarkModeRound} from '@vicons/material'

export const useDesignSettingStore = defineStore(
    'theme',
    () => {

        // 是否为暗系主题
        const isDarkTheme = ref(false)

        // 暗系主题-灯泡, 亮系主题-月牙
        const theme = computed(() => {
            if (isDarkTheme.value) {
                return {
                    name: darkTheme,
                    icon: LightbulbOutlined,
                    title:'dark'
                }
            }
            return {
                name: null,
                icon: DarkModeRound
            }

        })
        /**
         * 更改主题
         * @param dark {Boolean} 是否是暗系
         */
        const changeTheme = dark => {
            isDarkTheme.value = dark
        }
        return {
            isDarkTheme,
            theme,
            changeTheme
        }

    },
    {
        // 持久化存储
        persist: {
            storage: localStorage, // 本地存储
            paths: ['isDarkTheme'], // 将主题决定性值 持久化保存
        }
    })
