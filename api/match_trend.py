import logging
from datetime import date, datetime
from database import Database
from models.match_list_model import MatchListModel

logger = logging.getLogger(__name__)


async def match_trend_fetch():
	# 获取前30天的比赛
	time = 60 * 60 * 24 * (30 -1)
	today = date.today()
	dt = datetime.combine(today, datetime.min.time())
	now = int(dt.timestamp())

	session = None
	try:
		db = Database()
		session = db.get_session()
		print(now,now+time)
		ids = MatchListModel.get_30dyas_date_ids(session, now - time, now, 0)
		yield ids
	except Exception as e:
		logger.error(e)
	finally:
		if session: session.close()
