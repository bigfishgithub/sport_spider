import logging

from api.football_apis import get_team_stats_update

logger = logging.getLogger(__name__)


async def team_stats_update_fetch():
	try:
		response = await get_team_stats_update()
		if response['results']:
			yield response['results']
	except Exception as e:
		logger.error(e)
