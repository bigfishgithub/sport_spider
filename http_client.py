import asyncio

import httpx
from typing import Any, Dict, Optional
from config import Config
import logging
from tenacity import retry, wait_exponential, stop_after_attempt

class RetryableTransport(httpx.AsyncHTTPTransport):
    def __init__(self, retries: int = 3, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.retries = retries

    @retry(wait=wait_exponential(multiplier=1, min=4, max=10), stop=stop_after_attempt(3))
    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        try:
            return await super().handle_async_request(request)
        except (httpx.ConnectError, httpx.ReadError, httpx.WriteError, httpx.PoolTimeout) as exc:
            # 这里可以添加更多的异常类型，以确定哪些情况需要重试
            logging.warning(f"Transport error on {request.url}: {str(exc)}")
            raise exc

class HttpClient:
    _instance = None
    _lock = asyncio.Lock()

    @classmethod
    async def get_instance(cls):
        async with cls._lock:
            if cls._instance is None:
                cls._instance = cls()
            return cls._instance

    @retry(wait=wait_exponential(multiplier=1, min=4, max=10), stop=stop_after_attempt(3))
    async def get(self, url: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        logger = logging.getLogger(__name__)
        try:
            http_params = {
                "user": Config.API_KEY,
                "secret": Config.SECRET_KEY,
            }

            if params:
                http_params.update(params)
            transport = RetryableTransport(retries=3)
            limits = httpx.Limits(max_connections=100, max_keepalive_connections=20)
            async with httpx.AsyncClient(base_url=Config.API_URL, transport=transport, timeout=30.0,limits=limits) as client:
                response = await client.get(url, params=http_params)
                response.raise_for_status()  # 如果响应状态码不是 2xx，则抛出异常
                data = response.json()

                if 'err' in data:
                    logger.error(f"API returned error: {data.get('err')}")
                return data
        except httpx.RequestError as e:
            logger.error(f"请求错误 {e.request.url}: {str(e)}")
            raise e  # 可以选择抛出异常或根据业务逻辑处理
        except httpx.HTTPStatusError as e:
            logger.error(f"响应错误 {e.response.status_code} for {e.request.url}: {str(e)}")
            raise e  # 可以选择抛出异常或根据业务逻辑处理
        except Exception as e:
            logger.error(f"其他错误: {str(e)}")
            raise e  # 抛出异常以便上层逻辑处理


