import logging

from utils import Utils
from api.football_apis import get_coach

logger = logging.getLogger(__name__)


async def coach_list_fetch():
	try:
		params = {"id": -1, "limit": 1000, "time": 0}
		last_fetch = Utils.get_state_data("coach_list")
		params['time'] = last_fetch.max_time
		params['limit'] = last_fetch.limit
		response = await get_coach(params)
		if response['results']:
			yield response['results']

	except Exception as e:
		logger.error(e)
