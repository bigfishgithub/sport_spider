import logging

from api.football_apis import get_compensation_list
from database import Database
from models.compensation_list_model import CompensationListModel
from utils import Utils

logger = logging.getLogger(__name__)


class CompensationListJob:
	@classmethod
	async def run(cls, data):
		session = None
		try:
			db = Database()
			session = db.get_session()
			compensation = CompensationListModel(**data)
			compensation.insert(session)
		except Exception as e:
			if session: session.rollback()
			logger.error(e)
		finally:
			if session: session.close()
