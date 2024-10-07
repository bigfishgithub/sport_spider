import logging

from api.football_apis import get_competition_rule_list
from utils import Utils

logger = logging.getLogger(__name__)


async def competition_rule_list_fetch():
	params = {"id": -1, "limit": 1000, "time": 0}

	while True:
		try:
			last_fetch = Utils.get_state_data("competition_rule_list")
			params['time'] = last_fetch.max_time
			params['limit'] = last_fetch.limit
			response = await get_competition_rule_list(params)
			if response['results']:
				yield response['results']
			else:
				break
		except Exception as e:
			logging.error(e)
