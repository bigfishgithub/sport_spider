import logging

from api.football_apis import get_season_list
from database import Database
from models.table_detail_model import TableDetailModel

logger = logging.getLogger(__name__)


class TableDetailJob:

	@classmethod
	async def run(cls, data):
		params = {"id": data['season_id'], "time": 0, "limit": 1000}
		sesson_res = await get_season_list(params)
		if sesson_res:
			sesson_data = sesson_res['results'][0]
			session = None
			try:
				db = Database()
				session = db.get_session()
				data['competition_id'] = sesson_data['competition_id']
				table_detail = TableDetailModel(**data)
				table_detail.insert(session)
			except Exception as e:
				logger.error(e)
				logger.error(f"{data}")
				if session: session.rollback()
			finally:
				if session: session.close()
