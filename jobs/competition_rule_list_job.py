import logging

from database import Database
from models.competition_rule_list_model import CompetitionRuleListModel
from utils import Utils

logger = logging.getLogger(__name__)


class CompetitionRuleListJob:
	@classmethod
	async def run(cls, data):
		db = Database()
		session = db.get_session()
		try:
			for item in data:
				competition_rule_list = CompetitionRuleListModel(**item)
				competition_rule_list.insert(session)
				logger.info(f"insert data for competition_rule_list: {item}")
			Utils.update_last_data(CompetitionRuleListModel, "competition_rule_list")
		except Exception as e:
			if session: session.rollback()
			logger.error(e)
		finally:
			if session: session.close()

