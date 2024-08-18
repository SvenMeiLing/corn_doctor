# -*- coding: utf-8 -*-
# FileName: config.py
# Time : 2024/6/17 8:13
# Author: zzy
import os
from pathlib import Path

from dotenv import load_dotenv

# 项目根路径
PROJECT_PATH = Path(__file__).parent.parent.parent
# 应用程序路径
APP_PATH = PROJECT_PATH / "app"

load_dotenv()


def getenv_boolean(var_name, default_value=False):
    result = default_value
    env_value = os.getenv(var_name)
    if env_value is not None:
        result = env_value.upper() in ("TRUE", "1")
    return result


API_VERSION = "/api/v1"

SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    SECRET_KEY = os.urandom(32)

# token保质期
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8  # 60 minutes * 24 hours * 8 days = 8 days

# 服务器的配置
SERVER_NAME = os.getenv("SERVER_NAME")
SERVER_HOST = os.getenv("SERVER_HOST")
SERVER_PORT = os.getenv("SERVER_PORT")

# 支持的域(设置跨域),str->不同域以逗号分隔
BACKEND_CORS_ORIGINS = os.getenv(
    "BACKEND_CORS_ORIGINS"
)  # a string of origins separated by commas,
# e.g: "http://localhost, http://localhost:4200,
# http://localhost:3000, http://localhost:8080,
# http://local.dockertoolbox.tiangolo.com"

# 项目名称
PROJECT_NAME = os.getenv("PROJECT_NAME")

# Mysql数据库配置
MYSQL_SERVER = os.getenv("MYSQL_SERVER")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DB = os.getenv("MYSQL_DB")
SQLALCHEMY_DATABASE_URI = (
    f"mysql+aiomysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}/{MYSQL_DB}"
)

# Redis缓存配置
REDIS_HOST = os.getenv("REDIS_HOST", "127.0.0.1")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")

# smtp 配置 ----可忽略-----
SMTP_TLS = getenv_boolean("SMTP_TLS", True)
SMTP_PORT = None
_SMTP_PORT = os.getenv("SMTP_PORT")
if _SMTP_PORT is not None:
    SMTP_PORT = int(_SMTP_PORT)
SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
EMAILS_FROM_EMAIL = os.getenv("EMAILS_FROM_EMAIL")
EMAILS_FROM_NAME = PROJECT_NAME
EMAIL_RESET_TOKEN_EXPIRE_HOURS = 48
EMAIL_TEMPLATES_DIR = "/app/app/email-templates/build"
EMAILS_ENABLED = SMTP_HOST and SMTP_PORT and EMAILS_FROM_EMAIL

# --------------------------vision 配置--------------------------------
# 模型名称
MODEL_NAME = r"b2000_c15_int8_openvino_model"
MODEL_PATH = APP_PATH / "vision" / MODEL_NAME

# yolo.predict配置
PREDICT_CONFIG = {
    "conf": 0.7,
    "imgsz": 640,
}
# 用户上传图片保存地址
ORIGIN_IMG_PATH = APP_PATH / "vision" / "origin_imgs"

# 预测后图片物理路径
PREDICT_PATH = APP_PATH / "vision" / "predict"

# 图片访问URL, predict设置为了静态目录
MEDIA_ROOT = "http://127.0.0.1:8000/predict/"

# 初始化超级用户
FIRST_SUPERUSER = os.getenv("FIRST_SUPERUSER")
FIRST_SUPERUSER_PASSWORD = os.getenv("FIRST_SUPERUSER_PASSWORD")

USERS_OPEN_REGISTRATION = getenv_boolean("USERS_OPEN_REGISTRATION")
