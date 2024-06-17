# -*- coding: utf-8 -*-
# FileName: user.py
# Time : 2024/6/12 17:20
# Author: zzy
from typing import List

from pydantic import BaseModel, ConfigDict, Field, EmailStr, FilePath

from app.schemas.plant import Plant


class UserBase(BaseModel):
    username: str = Field(..., max_length=30)
    tel: str | None = Field(None, max_length=11)
    email: EmailStr | None = Field(None, max_length=30)
    avatar: FilePath | None = Field(None, max_length=30)


# innerAPI
class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    pass


class UserRegister(UserBase):
    username: str
    password: str


class UserInDBBase(UserBase):
    model_config = ConfigDict(from_attributes=True, use_enum_values=True)

    id: int
    plants: list[Plant] = []


class User(UserInDBBase):
    pass


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
