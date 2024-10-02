import logging

from api.football_apis import get_compensation_list
from database import Database
from models.compensation_list_model import CompensationListModel
from utils import Utils

logger = logging.getLogger(__name__)


class CompensationListJob:

	@staticmethod
	def __handle_response(response):
		if response['results']:
			data = response['results']
			session = None
			try:
				db = Database()
				session = db.get_session()
				for item in data:
					compensation = CompensationListModel(**item)
					compensation.insert(session)
					logger.info(f"insert data for compesation_list: {item}")
			except Exception as e:
				if session: session.rollback()
				logger.error(e)
			finally:
				if session: session.close()
			Utils.update_last_data(CompensationListModel, "compensation_list")

	@classmethod
	async def run(cls):
		params = {"id": -1, "limit": 1000, "time": 0}
		last_fetch = Utils.get_state_data("compensation_list")
		if last_fetch.max_time == 0:
			is_true = True
			while is_true:
				last_fetch = Utils.get_state_data("compensation_list")
				params['id'] = int(last_fetch.max_id)
				response = await get_compensation_list(params)
				if response['results']:
					cls.__handle_response(response)
				else:
					is_true = False
		else:
			last_fetch = Utils.get_state_data("compensation_list")
			if last_fetch:
				params['time'] = int(last_fetch.max_time)
				params['id'] = -1
			response = await get_compensation_list(params)
			cls.__handle_response(response)
