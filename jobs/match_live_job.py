import logging
from xml.sax import parse

from api.football_apis import get_match_live
from database import Database
from jobs.BaseJob import BaseJob
from models.match_live_model import MatchLiveModel
from models.player_list_model import PlayerListModel

logger = logging.getLogger(__name__)


class MatchLiveJob(BaseJob):
	@classmethod
	async def run(cls, ids):
		match_id = ids[0]
		try:
			response = await get_match_live({"id": match_id})
			if response['results']:
				data = response['results']
				db = Database()
				with db.get_session() as session:
					await cls.__process_incidents(session, data)
					match_live = MatchLiveModel(**data)
					match_live.insert(session)

		except Exception as e:
			logger.error(f"match_list_fetch: {e}")

	@classmethod
	async def __process_incidents(cls, session, item):
		if item.get('incidents'):
			for incident in item['incidents']:
				id_mapping = {
					'assist1_id': 'assist1_name',
					'assist2_id': 'assist2_name',
					'in_player_id': 'in_player_name',
					'out_player_id': 'out_player_name',
					'player_id': 'player_name'
				}
				for id_field, name_prefix in id_mapping.items():
					if incident.get(id_field):
						await cls.__map_player_names(session, incident, id_field, name_prefix)

	@classmethod
	async def __map_player_names(cls, session, incident, id_field, name_prefix):
		player_id = int(incident[id_field])

		try:
			player = PlayerListModel.get_player(session, player_id)
			print(f"-----{player.__dict__}")
			if not player:
				player = await cls.supplement_player_data(player_id)
			incident[f'{name_prefix}_vi'] = player.name_vi
			incident[f'{name_prefix}_en'] = player.name_en
		except Exception as e:
			logger.error(f"map_player_id: {player_id}")

