# -*- coding: utf-8 -*-
# FileName: recognition.py
# Time : 2024/6/9 10:27
# Author: zzy

from fastapi import FastAPI, File, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request
from websockets.http11 import Response

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:5173",
]
app.add_middleware(SessionMiddleware, secret_key="your_secret_key")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fake = [
    {
        "name": "葡萄黑腐病",
        "consuming": 0.111,
        "desc": "这是一种病"
    },
    {
        "name": "番茄叶斑病",
        "consuming": 0.222,
        "desc": "这是二种病"
    },
    {
        "name": "玉米钻心虫病",
        "consuming": 1.222,
        "desc": "这是三种病"
    },
]


@app.post("/upload")
async def create_file(
        file: list[UploadFile],
):
    for f in file:
        print(type(f))
        print(f.filename)

    return fake


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app)
