import logging
from database import Database
from models.competition_list_model import CompetitionListModel
from models.match_list_model import MatchListModel
from models.player_list_model import PlayerListModel
from models.season_list import SeasonListModel
from models.stage_list_model import StageListModel
from models.team_list_model import TeamListModel

logger = logging.getLogger(__name__)


class DeleteJob:

	@staticmethod
	def __delete_match(data):
		if not data:
			return
		db = Database()
		session = db.get_session()
		try:
			MatchListModel.delete(session, data)
			logger.info(f'Deleted match list{data}')
		except Exception as e:
			logger.error(e)
		finally:
			session.close()

	@staticmethod
	def __delete_team(data):
		if not data:
			return
		db = Database()
		session = db.get_session()
		try:
			TeamListModel.delete(session, data)
			logger.info(f'Deleted team list{data}')
		except Exception as e:
			logger.error(e)
		finally:
			session.close()

	@staticmethod
	def __delete_player(data):
		if not data:
			return
		db = Database()
		session = db.get_session()
		try:
			PlayerListModel.delete(session, data)
			logger.info(f'Deleted player list{data}')
		except Exception as e:
			logger.error(e)
		finally:
			session.close()

	@staticmethod
	def __delete_competition(data):
		if not data:
			return
		db = Database()
		session = db.get_session()
		try:
			CompetitionListModel.delete(session, data)
			logger.info(f'Deleted competition list{data}')
		except Exception as e:
			logger.error(e)
		finally:
			session.close()

	@staticmethod
	def __delete_season(data):
		if not data:
			return
		db = Database()
		session = db.get_session()
		try:
			SeasonListModel.delete(session, data)
			logger.info(f'Deleted season list{data}')
		except Exception as e:
			logger.error(e)
		finally:
			session.close()

	@staticmethod
	def __delete_stage(data):
		if not data:
			return
		db = Database()
		session = db.get_session()
		try:
			StageListModel.delete(session, data)
			logger.info(f'Deleted stage list{data}')
		except Exception as e:
			logger.error(e)
		finally:
			session.close()

	@classmethod
	async def run(cls, data):
		for item in data:
			try:
				cls.__delete_match(item.get('match'))
				cls.__delete_team(item.get('team'))
				cls.__delete_player(item.get('player'))
				cls.__delete_competition(item.get('competition'))
				cls.__delete_season(item.get('season'))
				cls.__delete_stage(item.get('stage'))
			except Exception as e:
				logger.error(e)
