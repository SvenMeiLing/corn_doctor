# -*- coding: utf-8 -*-
# FileName: cors_midd.py
# Time : 2024/6/9 11:15
# Author: zzy

from fastapi.middleware.cors import CORSMiddleware

from app.core.config import BACKEND_CORS_ORIGINS


def setup_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=BACKEND_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["GET", "POST", "OPTIONS", "PUT", "DELETE"],
        allow_headers=["*"],
    )
