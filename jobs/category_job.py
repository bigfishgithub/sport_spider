import logging

from api.football_apis import get_category
from database import Database
from models.category_model import CategoryModel
from enums.language_type import LanguageType
from utils import Utils

logger = logging.getLogger(__name__)


class CategoryJob:
	@staticmethod
	async def run():
		response = await get_category()
		if response.get('code') != 0:
			logger.error(response.get('err'))

		if response['results']:
			data = response['results']
			lang_data = await Utils.get_language(LanguageType.TYPE.value)
			for item in data:
				lang_list = list(filter(lambda lang: lang.get("id") == item.get("id"), lang_data))
				if lang_list:
					item['name_vi'] = lang_list[0].get('name_vi')
				item['name_vi'] = item['name_en']

				session = None
				try:
					db = Database()
					session = db.get_session()
					category = CategoryModel(**item)
					category.insert(session)
				except Exception as e:
					if session: session.rollback()
					logger.error(e)
				finally:
					if session: session.close()
