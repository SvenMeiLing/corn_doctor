# -*- coding: utf-8 -*-
# FileName: store.py
# Time : 2024/6/28 21:18
# Author: zzy
from app.crud.base import CRUDBase
from app.models.store import StoreOrm

store_crud = CRUDBase(StoreOrm)
