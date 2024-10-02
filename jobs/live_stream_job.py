import logging
from api.football_apis import get_live_stream
from database import Database
from models.live_stream_model import LiveStreamModel

logger = logging.getLogger(__name__)


class LiveStreamJob:

	@classmethod
	async def run(cls, data):
		db = Database()
		session = db.get_session()
		try:
			for item in data:
				live_stream = LiveStreamModel(**item)
				live_stream.insert(session)
		except Exception as e:
			if session: session.rollback()
			logger.error(e)
		finally:
			if session: session.close()
