# -*- coding: utf-8 -*-
# FileName: plant.py
# Time : 2024/6/13 21:08
# Author: zzy
from app.crud.base import CRUDBase
from app.models.plant import PlantOrm

plant_crud = CRUDBase(PlantOrm)
