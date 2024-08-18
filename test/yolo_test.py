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
]

if __name__ == '__main__':
    example = [
        {"name": "玉米条纹病毒", "year": [2024, 2025, 2026], "total": [22, 445, 355]},
        {"name": "玉米锈病", "year": [2024, 2025, 2026], "total": [22, 445, 355]},
        {"name": "玉米灰斑病", "year": [2024, 2025, 2026], "total": [22, 445, 355]},
    ]
    example2 = {
        "玉米条纹病毒": {
            "year": [2024, 2025, 2026], "total": [22, 445, 355]
        },
        "玉米锈病": {
            "year": [2024, 2025, 2026], "total": [22, 445, 355]
        },
        "玉米灰斑病": {
            "year": [2024, 2025, 2026], "total": [22, 445, 355]
        },
    }
    result = {}
    for index, plant in enumerate(data):
        year = plant["created_at"].split("-")[0]
        for _, dis in enumerate(plant["diseases"]):
            # 如果病害不存在则初始化进去
            if dis["name"] not in result:
                result[dis["name"]] = {"year": [year], "total": [1]}
            else:
                # 筛选新的年份加入(还剩total如何新增问题为解决)
                if year not in result[dis["name"]]["year"]:
                    result[dis["name"]]["year"].append(year)
                    result[dis["name"]]["total"].append(1)
                result[dis["name"]]["total"][_] += 1
    print(result)
