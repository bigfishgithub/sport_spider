import logging

from api.football_apis import get_match_lineup, get_team_list
from database import Database
from jobs.BaseJob import BaseJob
from jobs.team_list_job import TeamListJob
from models.match_lineup_model import MatchLineupModel
from models.match_list_model import MatchListModel
from models.player_list_model import PlayerListModel
from models.team_list_model import TeamListModel

logger = logging.getLogger(__name__)


class MatchListJob(BaseJob):
	@classmethod
	async def run(cls, data):
		db = Database()
		session = db.get_session()
		match_id = None
		try:
			team_list = [data['home_team_id'], data['away_team_id']]
			for team in team_list:
				if not TeamListModel.hasData(session, team):
					params = {"id": team, "limit": 1, "time": 0}
					team_response = await get_team_list(params)
					await TeamListJob.run(team_response['results'][0])

			if data['coverage']['lineup'] == 1:
				match_id = data['id']
			match_list = MatchListModel(**data)
			match_list.insert(session)
			if match_id:
				await cls.handle_lineup(match_id)
		except Exception as e:
			logger.error(e)
			session.rollback()
		finally:
			session.close()

	@staticmethod
	async def handle_lineup(match_id):
		# 处理阵容数据
		db = Database()
		session = db.get_session()
		response = await get_match_lineup({'id': match_id})
		if response['results']:
			resdata = response['results']
			resdata['match_id'] = match_id

			try:
				await MatchListJob.update_player_names(resdata, session)
				match_lineup_model = MatchLineupModel(**resdata)
				match_lineup_model.insert(session)
			except Exception as e:
				logger.error(e)


	@staticmethod
	async def update_player_names(resdata, session):
		for side in ['home', 'away']:
			if resdata[side]:
				for sub_item in resdata[side]:
					await MatchListJob.assign_player_names(sub_item, session)


	@classmethod
	async def assign_player_names(cls,sub_item, session):
		player_id = sub_item['id']
		player = PlayerListModel.get_player(session, player_id)
		if not player:
			player = await cls.supplement_player_data(player_id)
		sub_item['name_vi'] = player.name_vi or player.name_en
		sub_item['name_en'] = player.name_en

		if 'incidents' in sub_item:
			for incident in sub_item['incidents']:
				for key in ['player', 'in_player', 'out_player', 'assist1', 'assist2']:
					if incident.get(key):
						player_id = incident[key].get('id')
						player = PlayerListModel.get_player(session, player_id)
						if not player:
							player = await cls.supplement_player_data(player_id)
						incident[key]['name_vi'] = player.name_vi
						incident[key]['name_en'] = player.name_en

