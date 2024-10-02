import logging

from api.football_apis import get_deleted

logger = logging.getLogger(__name__)
async def delete_data_fetch():
	try:
		response =  await get_deleted()
		if response['results']:
			yield response['results']
	except Exception as e:
		logger.error("delete_data_fetch error:{}".format(e))
