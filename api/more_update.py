import logging

from api.football_apis import get_more_update

logger = logging.getLogger(__name__)
async def more_update_fetch():
	try:
		response = await get_more_update()
		if response['results']:
			yield response['results']
	except Exception as e:
		logger.error(f"match_list_fetch: {e}")
