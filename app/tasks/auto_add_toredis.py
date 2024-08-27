# -*- coding: utf-8 -*-
# FileName: auto_add_toredis.py
# Time : 2024/8/25 13:57
# Author: zzy
import random

from celery import Celery

from app.core.config import BACKEND, BROKER

app = Celery('tasks', backend=BACKEND, broker=BROKER)
app.conf.beat_schedule = {
    'add-flake-dis-every-second': {
        'task': 'auto_add_toredis.add_fake_dis',
        'schedule': 1.0,  # 每秒执行一次
    },
}
app.conf.timezone = 'Asia/Shanghai'


@app.task
def add_fake_dis():
    import redis
    r = redis.Redis()
    key = "daily_disease_ranking"

    # 要自增的成员及其增量
    member = ["玉米叶斑病", "玉米灰斑病", "玉米锈病", "玉米叶枯病", "玉米条纹病"]
    increment = random.randint(0, 99)  # 自增量

    # 自增操作
    r.zincrby(key, increment, member[random.randint(0, len(member) - 1)])
    r.close()
    return "success"
