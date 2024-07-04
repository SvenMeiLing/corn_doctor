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
                <Other :new-product="pesticide.slice(0,4)"/>
            </n-flex>
        </n-scrollbar>

    </n-layout>
</template>

<script setup>
// 代森锰锌,克草金,吡虫啉,唑醚-氟环唑,噻吗嗪,氟虫腈,氯虫苯甲酰胺,百菌清,阿维菌素
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
        shopName: "玉米医生",
        price: 17.3
    },
    {
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
        ],
        deliver: "包邮",
        shopName: "清风映绿",
        price: 27.3
    },
    {
        id: 3,
        name: "欣锐|甲基硫菌灵|抗真菌",
        desc: "甲基硫菌灵是一种广谱性杀菌剂，用于防治多种真菌性病害如叶斑病、枯萎病和白粉病。",
        img_src: "/src/assets/pesticide/甲基硫菌灵.jpg",
        usage_method: "在病害爆发初期进行叶面喷雾处理，使用浓度为每亩25-30克，每隔10-14天喷施一次，确保覆盖均匀。",
        precautions: [
            "避免吸入喷雾。",
            "不要在蜂箱附近或授粉高峰期使用。",
            "施药时需穿戴适当的防护装备，包括手套和口罩。",
            "按照当地法规处理容器和剩余产品。"
        ],
        deliver: "包邮",
        shopName: "麦田生物",
        price: 30
    },
    {
        id: 4,
        name: "农田守护|代森锰锌|含量高于50%",
        desc: "代森锰锌是一种广谱保护性杀菌剂，广泛用于防治多种作物的病害。",
        img_src: "/src/assets/pesticide/代森锰锌.png",
        usage_method: "在作物发病初期进行喷雾处理，稀释比例为每亩50-100克，每隔10-14天喷施一次。",
        precautions: [
            "避免与强酸或强碱混用。",
            "使用时需佩戴防护装备，避免药液接触皮肤和眼睛。",
            "避免在有风天气下喷施，以防药液飘移。",
            "按照标签说明安全使用和处置。"
        ],
        deliver: "包邮",
        shopName: "农田守护",
        price: 25.5
    },
    {
        id: 5,
        name: "田园卫士|克草金|含量高于95%",
        desc: "克草金是一种高效除草剂，主要用于防治多种禾本科和阔叶杂草。",
        img_src: "/src/assets/pesticide/克草金.png",
        usage_method: "在杂草生长初期进行喷雾处理，稀释比例为每亩50-100毫升，每隔20天喷施一次。",
        precautions: [
            "避免与其他药剂混用。",
            "使用时需佩戴防护装备，避免药液接触皮肤和眼睛。",
            "避免在有风天气下喷施，以防药液飘移。",
            "按照标签说明安全使用和处置。"
        ],
        deliver: "包邮",
        shopName: "田园卫士",
        price: 40.0
    },
    {
        id: 6,
        name: "庄稼卫士|吡虫啉|含量高于70%",
        desc: "吡虫啉是一种高效内吸性杀虫剂，广泛用于防治多种刺吸式害虫。",
        img_src: "/src/assets/pesticide/吡虫啉.png",
        usage_method: "在害虫初发期进行喷雾处理，稀释比例为每亩10-15克，每隔7-10天喷施一次。",
        precautions: [
            "避免与碱性物质混用。",
            "使用时需佩戴防护装备，避免药液接触皮肤和眼睛。",
            "避免在有风天气下喷施，以防药液飘移。",
            "按照标签说明安全使用和处置。"
        ],
        deliver: "包邮",
        shopName: "庄稼卫士",
        price: 18.0
    },
    {
        id: 7,
        name: "丰收卫士|唑醚-氟环唑|含量高于25%",
        desc: "唑醚-氟环唑是一种混合型广谱杀菌剂，用于防治多种真菌病害。",
        img_src: "/src/assets/pesticide/唑醚-氟环唑.png",
        usage_method: "在病害初发期进行喷雾处理，稀释比例为每亩30-50毫升，每隔10-14天喷施一次。",
        precautions: [
            "避免与碱性物质混用。",
            "使用时需佩戴防护装备，避免药液接触皮肤和眼睛。",
            "避免在有风天气下喷施，以防药液飘移。",
            "按照标签说明安全使用和处置。"
        ],
        deliver: "包邮",
        shopName: "丰收卫士",
        price: 32.0
    },
    {
        id: 8,
        name: "植保先锋|噻吗嗪|含量高于95%",
        desc: "噻吗嗪是一种选择性除草剂，适用于防治多种阔叶杂草。",
        img_src: "/src/assets/pesticide/噻吗嗪.jpg",
        usage_method: "在杂草生长初期进行喷雾处理，稀释比例为每亩20-30克，每隔14-21天喷施一次。",
        precautions: [
            "避免与其他除草剂混用。",
            "使用时需佩戴防护装备，避免药液接触皮肤和眼睛。",
            "避免在有风天气下喷施，以防药液飘移。",
            "按照标签说明安全使用和处置。"
        ],
        deliver: "包邮",
        shopName: "植保先锋",
        price: 28.0
    },
    {
        id: 9,
        name: "田园守护|氟虫腈|含量高于95%",
        desc: "氟虫腈是一种高效广谱杀虫剂，适用于防治多种咀嚼式害虫。",
        img_src: "/src/assets/pesticide/氟虫腈.jpg",
        usage_method: "在害虫初发期进行喷雾处理，稀释比例为每亩10-20克，每隔7-10天喷施一次。",
        precautions: [
            "避免与碱性物质混用。",
            "使用时需佩戴防护装备，避免药液接触皮肤和眼睛。",
            "避免在有风天气下喷施，以防药液飘移。",
            "按照标签说明安全使用和处置。"
        ],
        deliver: "包邮",
        shopName: "田园守护",
        price: 35.0
    },
    {
        id: 10,
        name: "绿色农场|氯虫苯甲酰胺|含量高于20%",
        desc: "氯虫苯甲酰胺是一种新型杀虫剂，对多种害虫具有高效防治效果。",
        img_src: "/src/assets/pesticide/氯虫苯甲酰胺.jpg",
        usage_method: "在害虫初发期进行喷雾处理，稀释比例为每亩15-25克，每隔10-14天喷施一次。",
        precautions: [
            "避免与其他杀虫剂混用。",
            "使用时需佩戴防护装备，避免药液接触皮肤和眼睛。",
            "避免在有风天气下喷施，以防药液飘移。",
            "按照标签说明安全使用和处置。"
        ],
        deliver: "包邮",
        shopName: "绿色农场",
        price: 42.0
    },
    {
        id: 11,
        name: "作物卫士|百菌清|含量高于50%",
        desc: "百菌清是一种广谱保护性杀菌剂，广泛用于防治多种作物的真菌病害。",
        img_src: "/src/assets/pesticide/百菌清.png",
        usage_method: "在病害初发期进行喷雾处理，稀释比例为每亩50-75克，每隔7-10天喷施一次。",
        precautions: [
            "避免与其他杀菌剂混用。",
            "使用时需佩戴防护装备，避免药液接触皮肤和眼睛。",
            "避免在有风天气下喷施，以防药液飘移。",
            "按照标签说明安全使用和处置。"
        ],
        deliver: "包邮",
        shopName: "作物卫士",
        price: 30.0
    },
    {
        id: 12,
        name: "虫害克星|阿维菌素|含量高于5%",
        desc: "阿维菌素是一种生物源杀虫剂，对多种害虫具有高效防治效果。",
        img_src: "/src/assets/pesticide/阿维菌素.png",
        usage_method: "在害虫初发期进行喷雾处理，稀释比例为每亩10-15毫升，每隔7-10天喷施一次。",
        precautions: [
            "避免与其他杀虫剂混用。",
            "使用时需佩戴防护装备，避免药液接触皮肤和眼睛。",
            "避免在有风天气下喷施，以防药液飘移。",
            "按照标签说明安全使用和处置。"
        ],
        deliver: "包邮",
        shopName: "虫害克星",
        price: 20.0
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

