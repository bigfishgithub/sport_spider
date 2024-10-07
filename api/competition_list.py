import logging

from api.football_apis import get_competition_list
from utils import Utils
logger = logging.getLogger(__name__)

async def competition_list_fetch():
	params = {"id": -1, "limit": 100, "time": 0}
	while True:
		last_fetch = Utils.get_state_data('competition_list')
		params['time'] = last_fetch.max_time
		params['limit'] = last_fetch.limit
		try:
			response = await get_competition_list(params)
			if response['results']:
				yield response['results']
			else:
				break
		except Exception as e:
			logger.error(e)
