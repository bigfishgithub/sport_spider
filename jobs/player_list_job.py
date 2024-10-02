import logging

from jobs.BaseJob import BaseJob
from models.player_list_model import PlayerListModel
from utils import Utils
from enums.language_type import LanguageType

logger = logging.getLogger(__name__)


class PlayerListJob(BaseJob):

	@classmethod
	async def run(cls,data):
		try:
			await cls.handle_lang(data, PlayerListModel, LanguageType.PLAYER.value)
			Utils.update_last_data(PlayerListModel, "player_list")
		except Exception as e:
			logger.error(e)
