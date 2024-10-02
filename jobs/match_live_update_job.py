import logging

from api.football_apis import get_match_live_update
from database import Database
from models.match_live_model import MatchLiveModel

logger = logging.getLogger(__name__)


class MatchLiveJobUpdate:

	@classmethod
	async def run(cls, data):
		session = None
		try:
			db = Database()
			session = db.get_session()
			for item in data:
				match_live = MatchLiveModel(**item)
				match_live.insert(session)
		except Exception as e:
			logger.error(e)
			if session: session.rollback()
		finally:
			if session: session.close()
