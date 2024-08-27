# coding=utf-8
data = [
    {
        "created_at": "2024-07-03",
        "diseases": [
            {
                "name": "玉米条纹病毒"
            },
            {
                "name": "玉米锈病"
            }
        ]
    },
    {
        "created_at": "2024-07-04",
        "diseases": [
            {
                "name": "玉米灰斑病"
            },
            {
                "name": "玉米条纹病毒"
            },
            {
                "name": "玉米锈病"
            }
        ]
    },
    {
        "created_at": "2025-07-04",
        "diseases": [

            {
                "name": "玉米锈病"
            }
        ]
    },
    {
        "created_at": "2023-07-04",
        "diseases": [

            {
                "name": "玉米锈病"
            }
        ]
    },
]

if __name__ == '__main__':
    def group_by_year(data: list[dict]):
        result = {}
        for index, plant in enumerate(data):
            plant: dict
            year = plant["created_at"].split("-")[0]
            for _, dis in enumerate(plant["diseases"]):
                # 如果病害不存在则初始化进去
                if dis["name"] not in result:
                    result[dis["name"]] = {"year": [year], "total": [1]}
                else:
                    # 如果年份不存在说明是第一次, 我们需要初始化年份, 并添加对应total的数量
                    if year not in result[dis["name"]]["year"]:
                        result[dis["name"]]["year"].append(year)
                        result[dis["name"]]["total"].append(1)
                    else:  # 如果病害年份存在,加对应年数的total+1, because -> year:[2024, 2025]<->total:[12, 20]
                        result[dis["name"]]["total"][
                            result[dis["name"]]["year"].index(year)  # 索引对应年份的total
                        ] += 1  # 对total+1
        return result
