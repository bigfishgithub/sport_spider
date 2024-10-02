import logging

from api.football_apis import get_stage_list
from database import Database
from models.stage_list_model import StageListModel
from utils import Utils

logger = logging.getLogger(__name__)


class StageListJob:
	@classmethod
	async def run(cls, data):
		session = None
		try:
			db = Database()
			session = db.get_session()
			for item in data:
				stage_list = StageListModel(**item)
				stage_list.insert(session)
				logger.info(f"insert data for stage_list: {item}")
			Utils.update_last_data(StageListModel, "stage_list")
		except Exception as e:
			logger.error(e)
			if session: session.rollback()
		finally:
			if session: session.close()

