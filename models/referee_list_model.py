import logging

from sqlalchemy import Integer, String
from sqlalchemy.orm import Session, Mapped,mapped_column

from models.base_model import BaseModel

logger = logging.getLogger(__name__)

class RefereeListModel(BaseModel):
	__tablename__ = 'sport_referee'

	id:Mapped[int] = mapped_column(Integer, primary_key=True)
	name_zh:Mapped[str] = mapped_column(String(50),nullable=False)
	name_zht:Mapped[str] = mapped_column(String(50),nullable=False)
	name_en:Mapped[str] = mapped_column(String(100),nullable=False)
	birthday:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	age:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	updated_at:Mapped[int] = mapped_column(Integer,nullable=False,default=0)

	def insert(self, session: Session):
		self.save(session)
		logger.info(f"sport_referee: 新增数据1条")