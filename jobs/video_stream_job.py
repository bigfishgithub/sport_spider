import logging
from database import Database
from models.video_stream_model import VideoStreamModel

logger = logging.getLogger(__name__)


class VideoStreamJob:
	@classmethod
	async def run(cls, data):

		session = None
		try:
			db = Database()
			session = db.get_session()
			for item in data:
				video_stream = VideoStreamModel(**item)
				video_stream.insert(session)
		except Exception as e:
			logger.error(e)
			if session: session.rollback()
		finally:
			if session: session.close()
