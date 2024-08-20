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
        "created_at": "2025-07-01",
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
    },
    {
        "created_at": "2024-07-05",
        "diseases": [
            {
                "name": "玉米灰斑病"
            }
        ]
    },
    {
        "created_at": "2024-07-06",
        "diseases": [
            {
                "name": "玉米灰斑病"
            }
        ]
    },
    {
        "created_at": "2024-07-07",
        "diseases": [
            {
                "name": "玉米灰斑病"
            }
        ]
    },
]
const getWeekRange = (date) => {
    const start = new Date(date);
    const day = start.getDay();
    const diff = start.getDate() - day - 6; // Get the previous week
    start.setDate(diff);
    start.setHours(0, 0, 0, 0);

    const end = new Date(start);
    end.setDate(start.getDate() + 6);
    end.setHours(23, 59, 59, 999);

    return { start, end };
};

export const groupBy = (data, type) => {
    const result = {};
    const now = new Date();

    if (type === 'week') {
        const { start, end } = getWeekRange(now);

        for (const item of data) {
            const date = new Date(item.created_at);
            if (date >= start && date <= end) {
                const day = date.toISOString().slice(0, 10); // Format date as YYYY-MM-DD

                if (!result[day]) {
                    result[day] = [];
                }

                for (const disease of item.diseases) {
                    const existingDisease = result[day].find(d => d.name === disease.name);
                    if (existingDisease) {
                        existingDisease.total += 1;
                    } else {
                        result[day].push({ name: disease.name, total: 1 });
                    }
                }
            }
        }

        // Transform result into an array of objects
        return Object.entries(result).map(([key, value]) => ({
            [key]: value
        }));
    } else {
        throw new Error('Invalid type. Use "week" for current week\'s previous week daily breakdown.');
    }
};

console.log(JSON.stringify(groupBy(data, "week")))
