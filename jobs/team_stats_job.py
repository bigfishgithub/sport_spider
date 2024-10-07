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
			team_stats = TeamStatsModel(**data)
			team_stats.insert(session)
		except Exception as e:
			logger.error(e)
			if session: session.rollback()
		finally:
			if session: session.close()
