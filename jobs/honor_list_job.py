import logging

from database import Database
from models.honor_list_model import HonorListModel
from utils import Utils

logger = logging.getLogger(__name__)


class HonorListJob:
	@classmethod
	async def run(cls, data):
		db = Database()
		session = db.get_session()
		try:
			for item in data:
				honor_list = HonorListModel(**item)
				honor_list.insert(session)
			Utils.update_last_data(HonorListModel, "honor_list")
		except Exception as e:
			if session: session.rollback()
			logger.error(e)
		finally:
			if session: session.close()
