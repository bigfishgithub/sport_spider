import logging

from api.football_apis import get_player_stats_update

logger = logging.getLogger(__name__)


async def player_status_update_fetch():
	try:
		response = await get_player_stats_update()
		if response:
			yield response['results']
	except Exception as e:
		logger.error(e)

