import logging

from sqlalchemy import func

from models.schedule_model import ScheduleModel
from database import Database

logger = logging.getLogger(__name__)


class Utils:
	@staticmethod
	def get_state(session, sport_type):
		return session.query(ScheduleModel).filter(ScheduleModel.code == sport_type).first()

	@classmethod
	def update_last_data(cls, model, name):
		db = Database()
		session = db.get_session()
		try:
			max_id = session.query(func.max(model.id)).scalar() or -1
			max_time = session.query(func.max(model.updated_at)).scalar() or 0
			print(f"=====  {name}========{max_id}==============")
			max_id = int(max_id) + 1
			max_time = int(max_time) + 1
			schedule_model = cls.get_state(session, name)
			if schedule_model:
				schedule_model.max_id = max_id
				schedule_model.max_time = max_time
				session.commit()
				logger.info(f"更新{schedule_model.code}最后一条记录时间为{max_time} id为:{max_id} ")
		except Exception as e:
			logger.error(e)
			session.rollback()
		finally:
			session.close()

	@staticmethod
	def get_state_data(name):
		session = None
		last_fetch = None
		try:
			db = Database()
			session = db.get_session()
			last_fetch = Utils.get_state(session, name)
		except Exception as e:
			logger.error(e)
		finally:
			session.close()
		return last_fetch


