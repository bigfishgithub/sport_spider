import logging

from api.football_apis import get_match_live_update
logger = logging.getLogger(__name__)

async def match_live_update_fetch():
	try:
		response = await get_match_live_update()
		if response['results']:
			yield response['results']
	except Exception as e:
		logger.error(f"match_list_fetch: {e}")
