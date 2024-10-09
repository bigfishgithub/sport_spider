import logging
from datetime import date, datetime
from api.football_apis import get_match_trend
from database import Database
from models.match_trend_model import MatchTrendModel
from models.match_list_model import MatchListModel

logger = logging.getLogger(__name__)


class MatchTrendJob:

	@classmethod
	async def run(cls, ids):
		match_id = ids[0]
		response = await get_match_trend({"id": match_id})
		if response['results']:
			data = response['results']
			session = None
			try:
				db = Database()
				session = db.get_session()
				data['match_id'] = match_id
				match_trend = MatchTrendModel(**data)
				match_trend.insert(session)
			except Exception as e:
				logger.error(e)
				if session: session.rollback()
			finally:
				if session: session.close()
