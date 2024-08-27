# -*- coding: utf-8 -*-
# FileName: token.py
# Time : 2024/8/27 22:35
# Author: zzy
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    username: str = None
