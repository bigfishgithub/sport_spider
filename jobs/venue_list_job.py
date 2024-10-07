import logging

from api.football_apis import get_venue_list
from database import Database
from models.venue_list_model import VenueListModel
from utils import Utils

logger = logging.getLogger(__name__)


class VenueListJob:
	@classmethod
	async def run(cls, data):
		session = None
		try:
			db = Database()
			session = db.get_session()
			venue_list = VenueListModel(**data)
			venue_list.insert(session)

		except Exception as e:
			logger.error(e)
			if session: session.rollback()
		finally:
			if session: session.close()

