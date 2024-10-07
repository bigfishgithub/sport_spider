import logging

from jobs.BaseJob import BaseJob
from models.player_list_model import PlayerListModel
from enums.language_type import LanguageType

logger = logging.getLogger(__name__)


class PlayerListJob(BaseJob):

	@classmethod
	async def run(cls,data):
		try:
			await cls.handle_lang(data, PlayerListModel, LanguageType.PLAYER.value)
		except Exception as e:
			logger.error(e)
