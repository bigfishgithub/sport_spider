import logging
from datetime import date, datetime
from api.football_apis import get_player_stats
from database import Database
from models.match_list_model import MatchListModel
logger = logging.getLogger(__name__)
async def player_stats_fetch():
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
			response = await get_player_stats({"id": match_id})
			if response:
				data = response['results']
				temp = []
				for item in data:
					temp.append({'match_id': match_id, "player_stats": item})
				yield temp
		except Exception as e:
			logger.error(e)
