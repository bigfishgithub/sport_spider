from api.football_apis import get_live_stream
import logging
logger = logging.getLogger(__name__)
async def live_stream_fetch():
	try:
		response = await get_live_stream()
		yield response['results']
	except Exception as e:
		logger.error(f"live_stream请求错误：{e}")
