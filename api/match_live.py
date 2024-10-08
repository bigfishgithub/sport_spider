import logging
from datetime import datetime, date

from api.football_apis import get_match_live
from database import Database
from models.match_list_model import MatchListModel

logger = logging.getLogger(__name__)

async def match_live_fetch():
	# 获取未开赛30天的数据
	t = 60 * 60 * 24 * 30
	today = date.today()
	dt = datetime.combine(today, datetime.min.time())

	max_t = int(dt.timestamp()) + 60 * 60 * 24
	min_t = max_t - t
	session = None
	ids = []
	try:
		db = Database()
		session = db.get_session()
		ids = MatchListModel.get_30dyas_date_ids(session, min_t, max_t, 2)
	except Exception as e:
		logger.error(e)
	finally:
		if session: session.close()

	id_list = [id_value[0] for id_value in ids]
	for match_id in id_list:
		try:
			response = await get_match_live({"id": match_id})
			if response['results']:
				yield response['results']
		except Exception as e:
			logger.error(f"match_list_fetch: {e}")

