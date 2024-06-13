# -*- coding: utf-8 -*-
# FileName: user.py
# Time : 2024/6/13 19:56
# Author: zzy
from app.crud.base import CRUDBase
from app.models.user import UserOrm

user_crud = CRUDBase(UserOrm)
