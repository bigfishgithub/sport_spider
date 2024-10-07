import logging

from jobs.BaseJob import BaseJob
from models.team_list_model import TeamListModel
from enums.language_type import LanguageType

logger = logging.getLogger(__name__)


class TeamListJob(BaseJob):
	@classmethod
	async def run(cls,data):
		try:
			await cls.handle_lang(data, TeamListModel, LanguageType.TEAM.value)
		except Exception as e:
			logger.error(e)
