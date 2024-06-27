<template>
    <n-layout class="h-full p-[20px]" embedded
              style="border: 1px solid red">
        <Search :goods-list="goodsList"></Search>
        <n-scrollbar>
            <n-flex class="h-full w-full flex-wrap xl:flex-nowrap">
                <!--第一部分-->
                <Recommend :recommend-list="seeds"></Recommend>

                <MainGoods :show-goods="pesticide" :slogan="'限时促销'"/>

                <!-- 第三部分 -->
                <Other/>
            </n-flex>
        </n-scrollbar>

    </n-layout>
</template>

<script setup>
import {CaretBackOutline, CaretForwardOutline} from '@vicons/ionicons5'
import {HotelClassTwotone} from '@vicons/material'
import NRLink from "@/components/NRLink.vue";
import RMB from "@/components/RMB.vue";
import Search from "@/views/Agriculture/Store/components/Search.vue";
import Recommend from "@/views/Agriculture/Store/components/Recommend.vue";
import MainGoods from "@/views/Agriculture/Store/components/MainGoods.vue";
import Other from "@/views/Agriculture/Store/components/Other.vue";
// 假设这是后端发来的数据/pesticide
const pesticide = ref([
    {
        id: 1,
        name: "玉米医生|三唑酮|含量高于20%",
        desc: "三唑酮是一种广谱性杀菌剂，主要用于防治多种作物的锈病和白粉病。",
        img_src: "/src/assets/pesticide/三唑酮.png",
        usage_method: "通常在发病初期进行喷雾处理，稀释比例为每亩20-30克，每隔7-10天喷施一次，连续喷施2-3次。",
        precautions: [
            "避免与碱性物质混用。",
            "使用时需佩戴防护装备，避免药液接触皮肤和眼睛。",
            "避免在有风天气下喷施，以防药液飘移。",
            "按照标签说明安全使用和处置。"
        ],
        deliver: "包邮",
        shopName: "玉米医生"
    }, {
        id: 2,
        name: "丙环唑|治疗叶斑",
        desc: "丙环唑是一种内吸性杀菌剂，对多种真菌性病害如锈病、叶斑病和枯萎病有效。",
        img_src: "/src/assets/pesticide/丙环唑.jpg",
        usage_method: "在病害初现时进行叶面喷雾处理，推荐浓度为每亩10-15克，每隔10-14天重复喷施，根据需要使用。",
        precautions: [
            "避免在花期使用，以免对传粉昆虫造成潜在伤害。",
            "施药时需穿戴防护服和防护装备。",
            "避免在水体附近喷施，以防污染。",
            "储存在阴凉干燥处，远离食物和动物饲料。"
        ]
    }, {
        id: 3,
        name: "甲基硫菌灵",
        desc: "甲基硫菌灵是一种广谱性杀菌剂，用于防治多种真菌性病害如叶斑病、枯萎病和白粉病。",
        img_src: "/src/assets/pesticide/甲基硫菌灵.jpg",
        usage_method: "在病害爆发初期进行叶面喷雾处理，使用浓度为每亩25-30克，每隔10-14天喷施一次，确保覆盖均匀。",
        precautions: [
            "避免吸入喷雾。",
            "不要在蜂箱附近或授粉高峰期使用。",
            "施药时需穿戴适当的防护装备，包括手套和口罩。",
            "按照当地法规处理容器和剩余产品。"
        ]
    }
])

const seeds = ref([
    {
        "id": 1,
        "name": "京科968",
        "img_src": "/src/assets/seed/京科968.jpg",
        "desc": "京科968是一种高产、抗病、适应性强的玉米品种，适合多种土壤和气候条件。",
        "price": 100
    },
    {
        "id": 2,
        "name": "先玉335",
        "img_src": "/src/assets/seed/先玉335.jpg",
        "desc": "先玉335具有高产稳产、抗逆性强的特点，适合大面积种植，深受农民喜爱。",
        "price": 120
    },
    {
        "id": 3,
        "name": "华农101",
        "img_src": "/src/assets/seed/华农101.jpg",
        "desc": "华农101是一种优质、高产的玉米品种，生育期适中，适应性广，抗病性强。",
        "price": 110
    },
    {
        "id": 4,
        "name": "登海605",
        "img_src": "/src/assets/seed/登海605.jpg",
        "desc": "登海605以其出色的抗病性和高产能力闻名，适合多种栽培方式，是农户的理想选择。",
        "price": 115
    },
    {
        "id": 5,
        "name": "郑单958",
        "img_src": "/src/assets/seed/郑单958.jpg",
        "desc": "郑单958是一种高产、抗病、稳产的玉米品种，具有良好的适应性和广泛的应用前景。",
        "price": 130
    }
])

const goodsList = ref([
    ...pesticide.value.map((value, _) => {
        return {label: value.name, value: value.name}
    }), ...seeds.value.map((value, _) => {
        return {label: value.name, value: value.name}
    })
])
onMounted(() => {
    console.log(goodsList.value)
})
</script>

<style scoped lang="scss">


.carousel-img {
  width: 100%;
  height: 100%;
  object-fit: fill;
}

:deep(.n-carousel__arrow) {
  background-color: rgba(58, 58, 58, 0.7);
}

:deep(.n-carousel__arrow:hover) {
  background-color: rgba(58, 58, 58, 1);
}

:deep(.n-breadcrumb-item__separator) {
  /*面包屑分隔符左右间距*/
  margin: 0 !important;
}

:deep(.n-breadcrumb-item__link) {
  color: rgb(255 255 255 / 52%) !important;
}

</style>

