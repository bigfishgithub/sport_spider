import logging

from api.football_apis import get_match_lineup, get_season_bracket, get_competition_table_detail, \
	get_competition_stats
from database import Database
from enums.date_type import DateType
from jobs.BaseJob import BaseJob
from models.match_lineup_model import MatchLineupModel
from models.player_list_model import PlayerListModel
from models.season_bracket_model import SeasonBracketModel
from models.table_detail_model import TableDetailModel
from models.competition_player_stats_model import CompetitionPlayerStatsModel
from models.competition_team_stats_model import CompetitionTeamStatsModel
from models.competition_shooters_stats_model import CompetitionShottersStatsModel

logger = logging.getLogger(__name__)


class MoreUpdateJob(BaseJob):
	@classmethod
	async def __handle_single_lineup(cls, data):
		for item in data:
			params = {"id": item['match_id'], "time": 0, "limit": 1000}
			response = await get_match_lineup(params)
			if response['results']:
				if isinstance(response['results'], list):
					resdata = response['results'][0]
				else:
					resdata = response['results']

				session = None
				try:
					db = Database()
					session = db.get_session()
					resdata['match_id'] = item['match_id']

					if resdata.get('home'):
						for sub_item in resdata['home']:
							player_id = sub_item.get("id")
							player = PlayerListModel.get_player(session, player_id)
							sub_item['name_vi'] = player.name_vi or player.name_en
							sub_item['name_en'] = player.name_en
							if sub_item.get('incidents'):
								for incident in sub_item['incidents']:
									if incident.get('player'):
										player_id = incident.get('player').get('id')
										player = PlayerListModel.get_player(session, player_id)
										print(player)
										if not player:
											player = await cls.supplement_player_data(player_id)
										incident['player']['name_vi'] = player.name_vi
										incident['player']['name_en'] = player.name_en
									if incident.get('in_player'):
										player_id = incident.get('in_player').get('id')
										player = PlayerListModel.get_player(session, player_id)
										if not player:
											player = await cls.supplement_player_data(player_id)
										incident['in_player']['name_vi'] = player.name_vi
										incident['in_player']['name_en'] = player.name_en
									if incident.get('out_player'):
										player_id = incident.get('out_player').get('id')
										player = PlayerListModel.get_player(session, player_id)
										if not player:
											player = await cls.supplement_player_data(player_id)
										incident['out_player']['name_vi'] = player.name_vi
										incident['out_player']['name_en'] = player.name_en
									if incident.get('assist1'):
										player_id = incident.get('assist1').get('id')
										player = PlayerListModel.get_player(session, player_id)
										if not player:
											player = await cls.supplement_player_data(player_id)
										incident['assist1']['name_vi'] = player.name_vi
										incident['assist1']['name_en'] = player.name_en

									if incident.get('assist2'):
										player_id = incident.get('assist2').get('id')
										player = PlayerListModel.get_player(session, player_id)
										if not player:
											player = await cls.supplement_player_data(player_id)
										incident['assist2']['name_vi'] = player.name_vi
										incident['assist2']['name_en'] = player.name_en
					if resdata.get('away'):
						for sub_item in resdata['away']:
							player_id = sub_item.get("id")
							player = PlayerListModel.get_player(session, player_id)
							if not player:
								player = await cls.supplement_player_data(player_id)
							sub_item['name_vi'] = player.name_vi or player.name_en
							sub_item['name_en'] = player.name_en
							if sub_item.get('incidents'):
								for incident in sub_item['incidents']:
									if incident.get('player'):
										player_id = incident.get('player').get('id')
										player = PlayerListModel.get_player(session, player_id)
										if not player:
											player = await cls.supplement_player_data(player_id)
										incident['player']['name_vi'] = player.name_vi
										incident['player']['name_en'] = player.name_en
									if incident.get('in_player'):
										player_id = incident.get('in_player').get('id')
										player = PlayerListModel.get_player(session, player_id)
										if not player:
											player = await cls.supplement_player_data(player_id)
										incident['in_player']['name_vi'] = player.name_vi
										incident['in_player']['name_en'] = player.name_en
									if incident.get('out_player'):
										player_id = incident.get('out_player').get('id')
										player = PlayerListModel.get_player(session, player_id)
										if not player:
											player = await cls.supplement_player_data(player_id)
										incident['out_player']['name_vi'] = player.name_vi
										incident['out_player']['name_en'] = player.name_en
									if incident.get('assist1'):
										player_id = incident.get('assist1').get('id')
										player = PlayerListModel.get_player(session, player_id)
										if not player:
											player = await cls.supplement_player_data(player_id)
										incident['assist1']['name_vi'] = player.name_vi
										incident['assist1']['name_en'] = player.name_en

									if incident.get('assist2'):
										player_id = incident.get('assist2').get('id')
										player = PlayerListModel.get_player(session, player_id)
										if player:
											player = await cls.supplement_player_data(player_id)
										incident['assist2']['name_vi'] = player.name_vi
										incident['assist2']['name_en'] = player.name_en
					match_lineup_model = MatchLineupModel(**resdata)
					match_lineup_model.insert(session)
				except Exception as e:
					logger.error(e)
					logger.error(f"{resdata}------__handle_single_lineup-------{item}")
					if session: session.rollback()
				finally:
					if session: session.close()

	@classmethod
	async def __handle_match_map(cls, data):
		for item in data:
			params = {"id": item['season_id']}
			response = await get_season_bracket(params)
			if response['results']:
				resdata = response['results']
				session = None
				try:
					db = Database()
					session = db.get_session()
					season_bracket_model = SeasonBracketModel(**resdata)
					season_bracket_model.insert(session)
				except Exception as e:
					logger.error(e)
					logger.error(f"{resdata}------__handle_match_map-------{item}")
					if session: session.rollback()
				finally:
					if session: session.close()

	@classmethod
	async def __handle_stadings(cls, data):
		for item in data:
			params = {"id": item['competition_id']}
			response = await get_competition_table_detail(params)
			if response['results']:
				resdata = response['results']
				session = None
				try:
					db = Database()
					session = db.get_session()
					resdata['season_id'] = item['season_id']
					resdata['competition_id'] = item['competition_id']
					team_stats_model = TableDetailModel(**resdata)
					team_stats_model.insert(session)
				except Exception as e:
					logger.error(e)
					logger.error(f"{str(resdata)}--------__handle_stadings-----{item}")
					if session: session.rollback()
				finally:
					if session: session.close()

	@classmethod
	async def __handle_competition_stats(cls, data):
		for item in data:
			params = {"id": item['competition_id']}
			response = await get_competition_stats(params)
			if response['results']:
				resdata = response['results']

				players_stats = resdata['players_stats']
				shooters = resdata['shooters']
				teams_stats = resdata['teams_stats']
				player_stats_list = [
					{"competition_id": item['competition_id'], "season_id": item['season_id'], **val} for
					val in players_stats]
				shooters_list = [
					{"competition_id": item['competition_id'], "season_id": item['season_id'], **val} for
					val in shooters]
				teams_stats_list = [
					{"competition_id": item['competition_id'], "season_id": item['season_id'], **val} for
					val in teams_stats]
				session = None
				try:
					db = Database()
					session = db.get_session()
					for players_stat in player_stats_list:
						players_stats = CompetitionPlayerStatsModel(**players_stat)
						players_stats.insert(session)
				except Exception as e:
					logger.error(e)
					if session: session.rollback()
				finally:
					if session: session.close()

					session = None
					try:
						db = Database()
						session = db.get_session()
						for shooters_stat in shooters_list:
							comtition_shotters_stats = CompetitionShottersStatsModel(**shooters_stat)
							comtition_shotters_stats.insert(session)
					except Exception as e:
						logger.error(e)
						if session: session.rollback()
					finally:
						if session: session.close()

					session = None
					try:
						db = Database()
						session = db.get_session()
						for teams_stat in teams_stats_list:
							competition_team_stats = CompetitionTeamStatsModel(**teams_stat)
							competition_team_stats.insert(session)
					except Exception as e:
						logger.error(e)
						if session: session.rollback()
					finally:
						if session: session.close()

	@classmethod
	async def run(cls, data):
		for k, v in data.items():
			# 单场阵容
			if k == str(DateType.SINGLE_GAME_LINEUP.value):
				await cls.__handle_single_lineup(v)

			# 对阵图
			if k == str(DateType.MATCH_MAP.value):
				await cls.__handle_match_map(v)

			# 积分榜
			if k == str(DateType.STANDINGS.value):
				await cls.__handle_stadings(v)

			#
			if k == str(DateType.SEASON_TEAM_PLAYER_STATISTICS.value):
				await cls.__handle_competition_stats(v)
