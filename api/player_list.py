import logging

from api.football_apis import get_player_list
from utils import Utils

logger = logging.getLogger(__name__)


async def player_list_fetch():
	params = {"id": -1, "limit": 1000, "time": 0}
	try:
		last_fetch = Utils.get_state_data("player_list")
		params['time'] = last_fetch.max_time
		params['limit'] = last_fetch.limit
		response = await get_player_list(params)
		if response['results']:
			yield response['results']
	except Exception as e:
		logger.error(f"player_list: {e}")
