import logging

from database import Database
from models.referee_list_model import RefereeListModel
from utils import Utils

logger = logging.getLogger(__name__)


class RefereeListJob:
	@classmethod
	async def run(cls, data):
		session = None

		try:

			db = Database()
			session = db.get_session()
			for item in data:
				print("===================================",item,"=========================")
				referee_list = RefereeListModel(**item)
				referee_list.insert(session)
				logger.info(f"insert data for referee_list:{item}")
			Utils.update_last_data(RefereeListModel, "referee_list")
		except Exception as ee:
			logger.error(ee)
			if session: session.rollback()
		finally:
			if session: session.close()

