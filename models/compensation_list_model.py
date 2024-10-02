import logging
from sqlalchemy import Integer, String, Text, JSON
from sqlalchemy.orm import mapped_column, Mapped, Session

from utils import Utils
from models.base_model import BaseModel

logger = logging.getLogger(__name__)



class CompensationListModel(BaseModel):
	__tablename__ = 'sport_compensation_list'

	id:Mapped[int]                  =       mapped_column(Integer,primary_key=True)
	history:Mapped[str]             =       mapped_column(JSON)
	recent:Mapped[str]              =       mapped_column(JSON)
	similar:Mapped[str]             =       mapped_column(JSON)
	updated_at:Mapped[int]          =       mapped_column(Integer)

	def insert(self, session: Session):
		self.save(session)
		logger.info(f"sport_compensation_list: 新增数据1条")





