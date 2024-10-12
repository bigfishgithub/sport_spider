import logging

from api.football_apis import get_stage_list
from database import Database
from models.stage_list_model import StageListModel
from utils import Utils

logger = logging.getLogger(__name__)


async def stage_list_fetch():
	params = {"id": -1, "limit": 1000, "time": 0}
	last_fetch = Utils.get_state_data("stage_list")
	params['time'] = last_fetch.max_time
	params['limit'] = last_fetch.limit
	try:
		response = await get_stage_list(params)
		if response['results']:
			yield response['results']
	except Exception as e:
		logger.error(e)
