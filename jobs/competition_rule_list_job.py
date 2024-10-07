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
			competition_rule_list = CompetitionRuleListModel(**data)
			competition_rule_list.insert(session)
		except Exception as e:
			if session: session.rollback()
			logger.error(e)
		finally:
			if session: session.close()

