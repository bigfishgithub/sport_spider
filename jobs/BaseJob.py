import logging

from api.football_apis import get_player_list, get_language
from database import Database

logger = logging.getLogger(__name__)


class BaseJob:
	@staticmethod
	async def get_language(lang_type, lang_id=0, lang_limit=0):
		params = {
			"id": lang_id,
			"type": str(lang_type),
			"limit": lang_limit
		}
		response = await get_language(params)
		data = response['results']

		return data

	@staticmethod
	async def handle_lang(data, model, _type):
		lang_data = await BaseJob.get_language(_type, data.get("id"), 1)
		if lang_data:
			data['name_vi'] = lang_data[0]['name_vi'] or data['name_en']
		else:
			data['name_vi'] = data['name_en']
		session = None
		try:
			db = Database()
			session = db.get_session()
			m = model(**data)
			m.insert(session)
		except Exception as e:
			logger.error(e)
			if session: session.rollback()
		finally:
			if session: session.close()

	@staticmethod
	async def supplement_player_data(player_id):
		from jobs.player_list_job import PlayerListJob
		player_params = {"id": player_id, "time": 0, "limit": 1}
		player_res = await get_player_list(player_params)
		if player_res['results']:
			player = player_res['results'][0]
			await PlayerListJob.run(player)
			return player
