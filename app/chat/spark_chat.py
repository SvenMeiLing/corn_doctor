# coding=utf-8
import os

from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler, AsyncChunkPrintHandler
from sparkai.core.messages import ChatMessage

try:
    from dotenv import load_dotenv
except ImportError:
    raise RuntimeError(
        'Python environment for SPARK AI is not completely set up: required package "python-dotenv" is missing.'
    ) from None

load_dotenv()


def chat(question):
    messages = [
        {
            "role": "user",
            "content": r"""
            现在你是一个名为"玉米医生"网站的客服, 
            请你以这个身份回答用户有关农业的问题:{question}
            """.format(question=question)
        }
    ]
    spark = ChatSparkLLM(
        spark_api_url=os.environ["SPARKAI_URL"],
        spark_app_id=os.environ["SPARKAI_APP_ID"],
        spark_api_key=os.environ["SPARKAI_API_KEY"],
        spark_api_secret=os.environ["SPARKAI_API_SECRET"],
        spark_llm_domain=os.environ["SPARKAI_DOMAIN"],
        request_timeout=30,
        streaming=True,
    )
    messages = [ChatMessage(role="user", content=messages[0]["content"])]
    handler = AsyncChunkPrintHandler()
    return spark.astream(messages, config={"callbacks": [handler]})
