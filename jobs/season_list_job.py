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
			season_list = SeasonListModel(**data)
			season_list.insert(session)

		except Exception as e:
			logger.error(e)
			if session: session.rollback()
		finally:
			if session: session.close()

