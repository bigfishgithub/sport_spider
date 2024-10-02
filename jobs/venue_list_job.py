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
			for item in data:
				venue_list = VenueListModel(**item)
				venue_list.insert(session)
				logger.info(f"insert data for venue_list: {item}")
			Utils.update_last_data(VenueListModel, "venue_list")
		except Exception as e:
			logger.error(e)
			if session: session.rollback()
		finally:
			if session: session.close()

