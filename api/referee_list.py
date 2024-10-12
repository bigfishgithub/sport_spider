import logging

from api.football_apis import get_referee_list
from utils import Utils

logger = logging.getLogger(__name__)


async def referee_list_fetch():
	params = {"id": -1, "limit": 1000, "time": 0}
	try:
		last_fetch = Utils.get_state_data("referee_list")
		params['time'] = last_fetch.max_time
		params['limit'] = last_fetch.limit
		response = await get_referee_list(params)
		if response['results']:
			yield response['results']
	except Exception as e:
		logger.error(e)
