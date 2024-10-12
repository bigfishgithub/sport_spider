import logging

from api.football_apis import get_team_stats
from database import Database
from models.team_stats_model import TeamStatsModel

logger = logging.getLogger(__name__)


class TeamStatsJob:
	@classmethod
	async def run(cls, ids):
		db = Database()
		session = db.get_session()
		match_id = ids[0]
		try:
			response = await get_team_stats({"id": match_id})
			if response['results']:
				data = response['results'][0]
				team_stats = TeamStatsModel(**data)
				team_stats.insert(session)
		except Exception as e:
			logger.error(e)
			session.rollback()
		finally:
			session.close()
