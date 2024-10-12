import logging
from datetime import date, datetime

from api.football_apis import get_video_stream
from database import Database
from models.match_list_model import MatchListModel

logger = logging.getLogger(__name__)


async def video_stream_fetch():
	today = date.today()
	min_t = datetime.combine(today, datetime.min.time())
	max_t = datetime.combine(today, datetime.max.time())
	session = None
	ids = []
	try:
		db = Database()
		session = db.get_session()
		ids = MatchListModel.get_30dyas_date_ids(session, min_t, max_t)
	except Exception as e:
		logger.error(e)
	finally:
		session.close()

	id_list = [id_value[0] for id_value in ids]
	for match_id in id_list:
		try:
			response = await get_video_stream({"id": match_id})
			if response['results']:
				data = response['results']
				for item in data:
					item['match_id'] = match_id
				yield data
		except Exception as e:
			logger.error(e)

