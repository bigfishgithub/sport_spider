import logging
from sqlalchemy import Integer, String
from models.base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, Session

logger = logging.getLogger(__name__)

class CountryModel(BaseModel):
	__tablename__ = 'sport_country'
	id:Mapped[int] = mapped_column(Integer, primary_key=True)
	category_id:Mapped[int] = mapped_column(Integer)
	name_zh:Mapped[str] = mapped_column(String(50), nullable=False)
	name_zht:Mapped[str] = mapped_column(String(50), nullable=False)
	name_en:Mapped[str] = mapped_column(String(50), nullable=False)
	name_vi:Mapped[str] = mapped_column(String(50), nullable=False,default='')
	logo:Mapped[str] = mapped_column(String(255), nullable=False)
	updated_at:Mapped[int] = mapped_column(Integer, nullable=False)

	def insert(self, session: Session):
		self.save(session)
		logger.info(f"sport_country: 新增数据1条")



