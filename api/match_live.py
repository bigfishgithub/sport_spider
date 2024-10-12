import logging
import time
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
	try:
		db = Database()
		session = db.get_session()
		ids = MatchListModel.get_30dyas_date_ids(session, min_t,int(time.time()))
		yield ids
	except Exception as e:
		logger.error(e)
	finally:
		if session: session.close()



