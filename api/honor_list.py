from api.football_apis import get_honor_list
from utils import Utils
import logging

logger = logging.getLogger(__name__)


async def honor_list_fetch():
	params = {"id": -1, "limit": 1000, "time": 0}
	last_fetch = Utils.get_state_data("honor_list")
	params['time'] = int(last_fetch.max_time)
	params['limit'] = last_fetch.limit
	try:
		response = await get_honor_list(params)
		if response['results']:
			yield response['results']
	except Exception as e:
		logger.error(f"live_stream请求错误：{e}")
