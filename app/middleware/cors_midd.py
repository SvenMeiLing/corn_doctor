# -*- coding: utf-8 -*-
# FileName: cors_midd.py
# Time : 2024/6/9 11:15
# Author: zzy
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import BACKEND_CORS_ORIGINS


def setup_cors(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,  # type: ignore
        allow_origins=BACKEND_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["GET", "POST", "OPTIONS", "PUT", "DELETE", "PATCH"],
        allow_headers=["*"]
    )
