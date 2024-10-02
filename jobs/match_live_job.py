import logging

from database import Database
from models.match_live_model import MatchLiveModel


logger = logging.getLogger(__name__)

class MatchLiveJob:
	@classmethod
	async def run(cls,data):
		session = None

		for item in data:
			try:
				db = Database()
				session = db.get_session()
				match_live = MatchLiveModel(**item)
				match_live.insert(session)
			except Exception as e:
				if session: session.rollback()
				logger.error(e)
			finally:
				if session: session.close()

