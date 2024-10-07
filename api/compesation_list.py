import logging

from api.football_apis import get_compensation_list
from database import Database
from models.compensation_list_model import CompensationListModel
from utils import Utils

logger = logging.getLogger(__name__)


async def compesation_list_fetch():
	params = {"id": -1, "limit": 1000, "time": 0}
	while True:
		last_fetch = Utils.get_state_data("compensation_list")
		params['time'] = int(last_fetch.max_time)
		params['limit'] = int(last_fetch.limit)
		try:
			response = await get_compensation_list(params)
			if response['results']:
				yield response['results']
			else:
				break
		except Exception as e:
			logger.error(e)
