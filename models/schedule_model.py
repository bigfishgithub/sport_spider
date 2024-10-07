import logging
from shlex import quote

from sqlalchemy import Integer, String, Sequence
from sqlalchemy.orm import Mapped, Session,mapped_column
from models.base_model import BaseModel

logger = logging.getLogger(__name__)

class ScheduleModel(BaseModel):
	__tablename__ = 'sport_schedule'
	id :Mapped[int] = mapped_column(Integer,primary_key=True)
	code:Mapped[str] = mapped_column(String(100))
	max_id:Mapped[int] = mapped_column(Integer,default=0)
	max_time:Mapped[int] = mapped_column(Integer,default=-1)
	limit:Mapped[int] = mapped_column(Integer,default=1000)

	def insert(self, session: Session):
		self.save(session)
		logger.info(f"sport_schedule: 新增数据1条")
