# -*- coding: utf-8 -*-
# FileName: user.py
# Time : 2024/6/12 17:20
# Author: zzy
from typing import List

from pydantic import BaseModel, ConfigDict, Field, EmailStr, FilePath

from app.schemas.plant import Plant


class UserBase(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=True)
    username: str = Field(..., max_length=30)
    tel: str = Field(None, max_length=11)
    email: EmailStr = Field(None, max_length=30)
    avatar: FilePath = Field(None, max_length=30)
    plants: List[Plant] = []


# innerAPI
class UserCreate(UserBase):
    password: str


class UserRegister(UserBase):
    username: str
    password: str
