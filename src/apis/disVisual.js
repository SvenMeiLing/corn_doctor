/* 
    *global console
    *FileName:disVisual.js
    *PATH:src/apis
    *Time: 2024/8/18 9:51
    *Author: zzy
*/
import request from "@/utils/http.js";

export function getDisVisual(mode) {
    return request('/plant/disease_visualization', {
        params: {
            mode: mode
        }
    })
}

export function getAllDiseaseCategory(){
    return request('/disease/category')

}
