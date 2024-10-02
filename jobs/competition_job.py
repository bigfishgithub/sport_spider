import logging

from database import Database
from enums.language_type import LanguageType
from models.competition_list_model import CompetitionListModel
from utils import Utils
from jobs.BaseJob import BaseJob

logger = logging.getLogger(__name__)


class CompetitionJob(BaseJob):
	@classmethod
	async def run(cls, data):
		await cls.handle_lang(data, CompetitionListModel, LanguageType.MATCH.value)
		Utils.update_last_data(CompetitionListModel, "competition_list")
