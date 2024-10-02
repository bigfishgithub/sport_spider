import logging

from api.football_apis import get_table_detail

logger = logging.getLogger(__name__)


async def table_detail_fetch():
	try:
		response = await get_table_detail()
		if response['results']:
			yield response['results']
	except Exception as e:
		logger.error(e)
