import logging
from datetime import date, datetime

from api.football_apis import get_match_analysis
from database import Database
from models.match_analysis_model import MatchAlalysisModel
from models.match_list_model import MatchListModel


logger = logging.getLogger(__name__)

class MatchAnalysisJob:
	@classmethod
	async def run(cls):

		# 获取未开赛30天的数据
		time = 60 * 60 * 24 * 30
		today = date.today()
		dt = datetime.combine(today, datetime.min.time())

		# 获取时间戳
		now = int(dt.timestamp())
		session = None
		try:
			db = Database()
			session = db.get_session()
			ids = MatchListModel.get_30dyas_date_ids(session,now, now + time,1)
		except Exception as e:
			logger.error(e)
		finally:
			if session:session.close()

		id_list = [id_value[0] for id_value in ids]
		for match_id in id_list:
			response = await get_match_analysis({"id":match_id})
			if response['results']:
				data = response['results']
				for item in data:
					item['match_id'] = match_id
					session = None
					try:
						db = Database()
						session = db.get_session()
						match_analysis =MatchAlalysisModel(**item)
						match_analysis.insert(session)
					except Exception as e:
						if session: session.rollback()
						logger.error(e)
					finally:
						if session: session.close()

