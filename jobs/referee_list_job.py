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
			referee_list = RefereeListModel(**data)
			referee_list.insert(session)
		except Exception as ee:
			logger.error(ee)
			if session: session.rollback()
		finally:
			if session: session.close()

