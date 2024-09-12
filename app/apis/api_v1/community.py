# -*- coding: utf-8 -*-
# FileName: community.py
# Time : 2024/9/11 13:57
# Author: zzy
from fastapi import APIRouter, Depends

from app.apis.deps.get_current_user import get_current_user

router = APIRouter(prefix="/plant", dependencies=[Depends(get_current_user)])
# todo: 社区有
#   提交帖子POST
#   更新帖子内容PATCH
#   删除帖子DELETE
#   获取推荐帖子GET(优先)
#   根据频道获取帖子GET
#   关注 收藏 点赞 评论 打赏

"""
帖子有哪些字段
post(标题,内容,帖子图片资源地址多张,用户id-外键)
comment()评论表:暂且不做过于复杂
like(count, post_id)点赞表:点赞数量关联内容id
channel(标题,帖子id-外键)
hot_list(标题,帖子id-外键)
"""
