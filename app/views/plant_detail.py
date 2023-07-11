# -*- coding: utf-8 -*-
# FileName: plant_detail.py
# Time : 2023/6/15 9:19
# Author: zzy
import pprint

from flask import g, jsonify
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import func

from app.models.plant_details import PlantDetailModel
from app.scripts.grouping import grouping, complete_list


class PlantDetail(MethodView):
    @jwt_required(locations="cookies")
    def get(self):
        # todo: title, count, 日期
        # 一周七天:   ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] 数据按月份
        # 葡萄黑腐病: [300, 200, 100, 300, 566, 300, 120]
        # 番茄叶斑病: [300, 200, 100, 300, 566, 300, 120]
        # 苹果黑星病: [300, 200, 100, 300, 566, 300, 120]
        email = get_jwt_identity()
        if email is not None:
            result = g.db_session.query(
                PlantDetailModel.title,
                func.coalesce(func.count(), 0),
                func.strftime("%w", PlantDetailModel.date)
            ). \
                group_by(
                PlantDetailModel.title,
                func.strftime("%w", PlantDetailModel.date)
            ).all()
            result = list(map(list, result))
            pprint.pprint(result)
            result = complete_list(result)
            return {
                "data": sorted(
                    list(grouping(result)), key=lambda it: [
                        '其他', '番茄叶斑病', '苹果黑星病', '葡萄黑腐病',
                        '健康', '玉米大斑病', '玉米灰斑病', '玉米锈病', '玉米钻心虫病'
                    ].index(it[0][0][0])
                )
            }
        return {"error": "身份验证失败, 请重新登录"}
