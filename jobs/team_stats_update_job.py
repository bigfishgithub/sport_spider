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
			team_stats = TeamStatsModel(**data)
			team_stats.insert(session)
		except Exception as e:
			session.rollback()
			logger.error(f"批量保存时发生错误: {e}")
		finally:
			session.close()
