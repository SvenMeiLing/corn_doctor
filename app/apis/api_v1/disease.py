# -*- coding: utf-8 -*-
# FileName: disease.py
# Time : 2024/6/13 20:52
# Author: zzy
from aioredis import Redis
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request

from app.apis.deps.get_cache import get_cache
from app.apis.deps.get_db import get_db
from app.crud.disease import disease_crud
from app.schemas.disease_pest import DiseaseBase, Disease, DiseaseInDBBase

router = APIRouter(prefix="/disease")


@router.get("/", response_model=Disease)
async def get_disease(
        disease_id: int, db_session: AsyncSession = Depends(get_db)
):
    """通过id查询病害"""
    disease = await disease_crud.get(db_session, disease_id)
    if not disease:
        raise HTTPException(status_code=404, detail="DiseaseBase not found")
    return disease


@router.get("/plants", response_model=DiseaseInDBBase)
async def get_disease(
        disease_id: int, db_session: AsyncSession = Depends(get_db)
):
    """通过id查询病害,包括患此病害的植物"""
    disease = await disease_crud.get_with_relations(db_session, disease_id, "plants")
    if not disease:
        raise HTTPException(status_code=404, detail="DiseaseBase not found")
    print(disease)
    return disease


@router.get("/category", response_model=list[Disease])
async def get_all_disease_category(
        db_session: AsyncSession = Depends(get_db)
):
    """获取所有病害类别"""
    dis_lst = await disease_crud.get_multi(db_session)
    return dis_lst


@router.get("/ranking")
async def get_disease_ranking(
        db_session: AsyncSession = Depends(get_db),
        *,
        request: Request
):
    """
    获取病害排行
    todo: 先从缓存中获取, 如果没有再查找数据库
    """
    key = "daily_disease_ranking"
    cache: Redis = request.app.state.redis
    top_diseases = await cache.zrevrange(key, 0, -1, withscores=True)

    # 如果缓存中没有从mysql获取数据
    if top_diseases is None:
        result = await disease_crud.get_ranking(db_session)
        # todo:并持久化到缓存中
        return result
    return top_diseases


@router.post("/", response_model=Disease)
async def create_disease(
        disease_in: DiseaseBase, db_session: AsyncSession = Depends(get_db)
):
    """新增病害"""
    disease = await disease_crud.create(db_session, obj_in=disease_in)
    return disease
