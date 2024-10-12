import logging

from api.football_apis import get_player_stats
from database import Database
from models.player_stats_model import PlayerStatsModel

logger = logging.getLogger(__name__)


class PlayerStatsJob:
	@classmethod
	async def run(cls, ids):
		session = None
		match_id = ids[0]
		try:
			response = await get_player_stats({"id": match_id})
			if response:
				data = response['results']
				db = Database()
				session = db.get_session()
				for item in data:
					obj = {'match_id': match_id, "player_stats": item}
					player_stats = PlayerStatsModel(**obj)
					player_stats.insert(session)
		except Exception as e:
			logger.error(e)
			if session: session.rollback()
		finally:
			if session: session.close()
