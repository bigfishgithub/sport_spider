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
			for item in data:
				player_stats = PlayerStatsModel(**item)
				player_stats.insert(session)
				logger.info(f"insert data for player_stats: {item}")
		except Exception as e:
			logger.error(e)
			if session: session.rollback()
		finally:
			if session: session.close()
