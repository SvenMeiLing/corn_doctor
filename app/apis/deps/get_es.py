# -*- coding: utf-8 -*-
# FileName: get_es.py
# Time : 2024/9/11 15:06
# Author: zzy
import asyncio
from functools import lru_cache  # 一个缓存装饰器， 在网上找寻的方法

from elasticsearch import AsyncElasticsearch

"""
 'hosts': 'https://127.0.0.1:9200',
        'basic_auth': ('zzy', '168168956'),
        'ca_certs': str(CORE_DIR / "http_ca.crt")  # 指定证书文件路径
"""


@lru_cache(maxsize=128)
def get_es() -> AsyncElasticsearch:
    """获取ES连接对象"""
    from app.core import config
    return AsyncElasticsearch(
        config.ES_HOSTS, basic_auth=config.ES_BASIC_AUTH,
        ca_certs=config.CA_CERTS
    )


if __name__ == '__main__':
    print(asyncio.run(get_es().search(index="artist", body={
        "query": {
            "nested": {
                "path": "album.music",
                "query": {
                    "bool": {
                        "should": [
                            {
                                "match": {
                                    "album.music.lyric": {
                                        "query": "节奏",
                                        "boost": 3
                                    }
                                }
                            },
                            {
                                "match": {
                                    "album.music.name": {
                                        "query": "节奏",
                                        "boost": 2
                                    }
                                }
                            }
                        ]
                    }
                }
            }
        },
        "_source": ["name", "album.name", "album.music.name"]
    })))
