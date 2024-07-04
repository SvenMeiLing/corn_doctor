# -*- coding: utf-8 -*-
# FileName: pest.py
# Time : 2024/7/4 15:28
# Author: zzy

from app.crud.base import CRUDBase
from app.models.plant import PestOrm

pest_crud = CRUDBase(PestOrm)
