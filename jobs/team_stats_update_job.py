import logging

from api.football_apis import get_team_stats_update
from database import Database
from models.team_stats_model import TeamStatsModel

logger = logging.getLogger(__name__)


class TeamStatsUpdateJob:
	@classmethod
	async def run(cls, data):
		session = None
		try:
			db = Database()
			session = db.get_session()
			for item in data:
				team_stats = TeamStatsModel(**item)
				team_stats.insert(session)
				logger.info(f"insert data for venue_list: {item}")
		except Exception as e:
			session.rollback()
			logger.error(f"批量保存时发生错误: {e}")
		finally:
			session.close()
