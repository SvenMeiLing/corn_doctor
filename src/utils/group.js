/* 
    *global console
    *FileName:group.js
    *PATH:src/utils
    *Time: 2024/8/17 21:44
    *Author: zzy
*/
let data = [
    {
        "created_at": "2025-07-03",
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
            }
        ]
    },
    {
        "created_at": "2024-07-04",
        "diseases": [
            {
                "name": "玉米灰斑病"
            }
        ]
    }
]
const getWeekNumber = (date) => {
    const start = new Date(date.getFullYear(), 0, 1);
    const diff = date - start + ((start.getDay() + 1) * 24 * 60 * 60 * 1000);
    const oneWeek = 7 * 24 * 60 * 60 * 1000;
    return Math.ceil(diff / oneWeek);
};

const groupBy = (data, type) => {
    const result = {};
    const now = new Date();
    const currentYear = now.getFullYear();
    const startDate = new Date(now.setDate(now.getDate() - 7)); // Default start date for weeks

    for (const item of data) {
        const date = new Date(item.created_at);
        let key;

        switch (type) {
            case 'year':
                key = date.getFullYear();
                break;
            case 'month':
                key = `${date.getFullYear()}-${(date.getMonth() + 1).toString().padStart(2, '0')}`;
                break;
            case 'week':
                if (date >= startDate) {
                    const year = date.getFullYear();
                    const week = getWeekNumber(date);
                    key = `${year}-W${week}`;
                }
                break;
            default:
                throw new Error('Invalid type. Use "year", "month", or "week".');
        }

        if (key) {
            if (!result[key]) {
                result[key] = [];
            }

            for (const disease of item.diseases) {
                const existingDisease = result[key].find(d => d.name === disease.name);
                if (existingDisease) {
                    existingDisease.total += 1;
                } else {
                    result[key].push({ name: disease.name, total: 1 });
                }
            }
        }
    }

    return Object.entries(result).map(([key, value]) => ({
        [key]: value
    }));
};

console.log(JSON.stringify(groupBy(data, "week")))
