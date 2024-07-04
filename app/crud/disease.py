# -*- coding: utf-8 -*-
# FileName: disease.py
# Time : 2024/6/13 20:52
# Author: zzy

from app.crud.base import CRUDBase
from app.models.plant import DiseaseOrm

disease_crud = CRUDBase(DiseaseOrm)
