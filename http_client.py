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
            raise exc

class HttpClient:

    def __init__(self, base_url: str = Config.API_URL):
        """配置http"""
        transport = RetryableTransport(retries=3)
        self.client = httpx.AsyncClient(base_url=base_url, transport=transport, timeout=None)

    async def get(self, url: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        logger = logging.getLogger(__name__)
        try:
            http_params = {
                "user": Config.API_KEY,
                "secret": Config.SECRET_KEY,
            }

            if params:
                http_params.update(params)

            response = await self.client.get(url, params=http_params)
            response.raise_for_status()  # 如果响应状态码不是 2xx，则抛出异常
            data = response.json()

            if 'err' in data:
                logging.error(data.get('err'))
            return data
        except httpx.RequestError as e:
            # 记录请求错误
            logger.error(f"请求错误 {e.request.url}: {str(e)}")
        except httpx.HTTPStatusError as e:
            # 记录响应错误，例如 4xx 或 5xx 错误
            logger.error(f"响应错误 {e.response.status_code} for {e.request.url}: {str(e)}")
        except Exception as e:
            # 捕获其他错误
            logger.error(f"其他错误: {str(e)}")