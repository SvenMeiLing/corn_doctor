# -*- coding: utf-8 -*-
# FileName: hasher.py
# Time : 2024/7/1 14:11
# Author: zzy
import hashlib


def gen_hashed(file_byt: bytes):
    md5 = hashlib.md5(file_byt)
    return md5.hexdigest()
