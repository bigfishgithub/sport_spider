import logging

from api.football_apis import get_match_list
from database import Database
from models.match_list_model import MatchListModel
from utils import Utils

logger = logging.getLogger(__name__)


class MatchListJob:
	@staticmethod
	async def run(data):
		db = Database()
		session = db.get_session()
		try:
			for item in data:
				match_list = MatchListModel(**item)
				match_list.insert(session)
			Utils.update_last_data(MatchListModel, "match_list")
		except Exception as e:
			if session: session.rollback()
			logger.error(e)
		finally:
			if session: session.close()
