import logging

from database import Database
from models.season_list import SeasonListModel
from utils import Utils

logger = logging.getLogger(__name__)


class SeasonListJob:
	@classmethod
	async def run(cls, data):
		session = None
		try:
			db = Database()
			session = db.get_session()
			for item in data:
				season_list = SeasonListModel(**item)
				season_list.insert(session)
				logger.info(f"insert data for season_list: {item}")
			Utils.update_last_data(SeasonListModel, "season_list")

		except Exception as e:
			logger.error(e)
			if session: session.rollback()
		finally:
			if session: session.close()

