import logging
from api.football_apis import get_country_list
from enums.language_type import LanguageType
from jobs.BaseJob import BaseJob
from models.country_model import CountryModel

logger = logging.getLogger(__name__)


class CountryJob(BaseJob):
	@classmethod
	async def run(cls):
		response = await get_country_list()
		if response['results']:
			data = response['results']
			for item in data:
				await cls.handle_lang(item, CountryModel, LanguageType.COUNTRY.value)
