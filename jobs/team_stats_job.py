import logging
from database import Database
from models.team_stats_model import TeamStatsModel

logger = logging.getLogger(__name__)


class TeamStatsJob:
	@classmethod
	async def run(cls, data):

		session = None
		try:
			db = Database()
			session = db.get_session()
			for item in data:
				team_stats = TeamStatsModel(**item)
				team_stats.insert(session)
				logger.info(f"insert data for team_stats: {item}")
		except Exception as e:
			logger.error(e)
			if session: session.rollback()
		finally:
			if session: session.close()
