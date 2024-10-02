import logging

from api.football_apis import get_team_list
from jobs.BaseJob import BaseJob
from models.team_list_model import TeamListModel
from utils import Utils
from enums.language_type import LanguageType

logger = logging.getLogger(__name__)


class TeamListJob(BaseJob):
	@classmethod
	async def run(cls,data):
		try:
			await cls.handle_lang(data, TeamListModel, LanguageType.TEAM.value)
			Utils.update_last_data(TeamListModel, "team_list")
		except Exception as e:
			logger.error(e)
