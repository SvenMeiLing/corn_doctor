# -*- coding: utf-8 -*-
# FileName: store.py
# Time : 2024/6/28 21:28
# Author: zzy
from pydantic import BaseModel, ConfigDict, Field


class StoreBase(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)
    name: str = Field(..., example="玉米店铺", title="店铺名称")
    logo_img: str = Field(..., title="店铺封面图片")


class StoreInDBBase(StoreBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    products: list['ProductInDBBase'] = []


class Store(StoreInDBBase):
    pass


class CategoryInDBBase(BaseModel):
    # 商品分类orm
    model_config = ConfigDict(from_attributes=True)

    id: int
    products: list['ProductInDBBase'] = []


class ProductBase(BaseModel):
    name: str = Field(..., max_length=32, title='商品名称', example='代森锰锌')
    price: float = Field(..., title='商品价格', example='11.2')
    stock_quantity: int = Field(..., title='商品库存', example="300")
    brand: str = Field(..., max_length=64, title='品牌')
    status: str = Field(..., max_length=16, title='状态')
    image_url: str = Field(..., title='商品图片', description='多张图片以逗号分隔')
    shipping_method: str =


class ProductInDBBase(BaseModel):
    # 商品orm
    model_config = ConfigDict(from_attributes=True)

    id: int
