import logging
from database import Database
from models.player_stats_model import PlayerStatsModel

logger = logging.getLogger(__name__)


class PlayerStatsUpdateJob:
	@classmethod
	async def run(cls, data):
		session = None
		try:
			db = Database()
			session = db.get_session()
			player_stats = PlayerStatsModel(**data)
			player_stats.insert(session)
		except Exception as e:
			logger.error(e)
			if session: session.rollback()
		finally:
			if session: session.close()
