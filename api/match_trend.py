import logging
import time
from datetime import date, datetime
from database import Database
from models.match_list_model import MatchListModel

logger = logging.getLogger(__name__)


async def match_trend_fetch():
	# 获取前30天的比赛
	today = date.today()
	dt = datetime.combine(today, datetime.min.time())
	today_12 = int(dt.timestamp())

	session = None
	try:
		db = Database()
		session = db.get_session()

		# 分批查询，每次获取 batch_size 条记录
		ids = MatchListModel.get_30dyas_date_ids(session, today_12, time.time())
		yield ids

	except Exception as e:
		logger.error(f"Error fetching match trend data: {e}")
	finally:
		if session: session.close()
