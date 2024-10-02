import logging
import traceback

from api.football_apis import get_more_update, get_match_lineup, get_season_bracket, get_competition_table_detail, \
	get_competition_stats
from database import Database
from enums.date_type import DateType
from models.match_lineup_model import MatchLineupModel
from models.season_bracket_model import SeasonBracketModel
from models.table_detail_model import TableDetailModel
from models.team_stats_model import TeamStatsModel
from models.competition_player_stats_model import CompetitionPlayerStatsModel
from models.competition_team_stats_model import CompetitionTeamStatsModel
from models.competition_shooters_stats_model import CompetitionShottersStatsModel

logger = logging.getLogger(__name__)


class MoreUpdateJob:

	@staticmethod
	def __get_session():
		db = Database()
		return db.get_session()

	@classmethod
	async def __handle_single_lineup(cls, data):
		for item in data:
			params = {"id": item['match_id'], "time": 0, "limit": 1000}
			response = await get_match_lineup(params)
			if response['results']:
				resdata = response['results']
				session = None
				try:
					session = cls.__get_session()
					resdata['match_id'] = item['match_id']

					match_lineup_model = MatchLineupModel(**resdata)
					match_lineup_model.insert(session)
				except Exception as e:
					logger.error(e)
					logger.error(f"{resdata}-------------{item}")
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
					session = cls.__get_session()
					season_bracket_model = SeasonBracketModel(**resdata)
					season_bracket_model.insert(session)
				except Exception as e:
					logger.error(e)
					logger.error(f"{resdata}-------------{item}")
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
					session = cls.__get_session()
					resdata['season_id'] = item['season_id']
					resdata['competition_id'] = item['competition_id']
					team_stats_model = TableDetailModel(**resdata)
					team_stats_model.insert(session)
				except Exception as e:
					logger.error(e)
					logger.error(f"{str(resdata)}-------------{item}")
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

				for players_stat in player_stats_list:
					session = None

					try:
						session = cls.__get_session()
						players_stats = CompetitionPlayerStatsModel(**players_stat)
						players_stats.insert(session)
					except Exception as e:
						logger.error(e)
						logger.error(f"{players_stat}-------------{item}")
						if session: session.rollback()
					finally:
						if session: session.close()

				for shooters_stat in shooters_list:
					session = None
					try:
						session = cls.__get_session()
						comtition_shotters_stats = CompetitionShottersStatsModel(**shooters_stat)
						comtition_shotters_stats.insert(session)
					except Exception as e:
						logger.error(e)
						logger.error(f"{shooters_stat}-------------{item}")
						if session: session.rollback()
					finally:
						if session: session.close()

				for teams_stat in teams_stats_list:
					session = None
					try:
						session = cls.__get_session()
						competition_team_stats = CompetitionTeamStatsModel(**teams_stat)
						competition_team_stats.insert(session)
					except Exception as e:
						logger.error(e)
						logger.error(f"{teams_stat}-------------{item}")
						if session: session.rollback()
					finally:
						if session: session.close()

	@classmethod
	async def run(cls, data):
		data = data[0]
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
