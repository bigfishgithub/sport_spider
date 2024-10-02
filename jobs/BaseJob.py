import logging

from database import Database
from utils import Utils

logger = logging.getLogger(__name__)


class BaseJob:
	@staticmethod
	async def handle_lang(data, model, _type):
		for item in data:
			lang_data = await Utils.get_language(_type, item.get("id"), 1)
			if lang_data:
				item['name_vi'] = lang_data[0]['name_vi'] or item['name_en']
			else:
				item['name_vi'] = item['name_en']
			session = None
			try:
				db = Database()
				session = db.get_session()
				m = model(**item)
				m.insert(session)
				logger.info(f"language:{item}")
			except Exception as e:
				logger.error(e)
				if session: session.rollback()
			finally:
				if session: session.close()
