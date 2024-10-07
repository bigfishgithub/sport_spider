import logging

from utils import Utils
from api.football_apis import get_coach
from models.coach_model import CoachModel
from database import Database

logger = logging.getLogger(__name__)


class CoachJob:
	@classmethod
	async def run(cls, data):
		datebase = Database()
		session = datebase.get_session()
		try:
			coach_model = CoachModel(**data)
			coach_model.save(session)
		except Exception as e:
			if session: session.rollback()
			logger.error(e)
		finally:
			if session: session.close()
