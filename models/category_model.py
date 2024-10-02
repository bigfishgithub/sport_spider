from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Session, Mapped
import logging
from models.base_model import BaseModel

logger = logging.getLogger(__name__)
class CategoryModel(BaseModel):
	__tablename__   =   'sport_category'
	id:Mapped[int]                =   mapped_column(Integer, primary_key=True)
	name_zh:Mapped[str]           =   mapped_column(String(50),nullable = False)
	name_zht:Mapped[str]          =   mapped_column(String(50),nullable = False)
	name_en:Mapped[str]           =   mapped_column(String(50),nullable = False)
	name_vi:Mapped[str]           =   mapped_column(String(50),default='')
	updated_at:Mapped[int]        =   mapped_column(Integer,nullable=False)

	def insert(self, session: Session):
		self.save(session)
		logger.info(f"sport_category: 新增数据1条")

