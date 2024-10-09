import logging
import time

from sqlalchemy import Integer, String, JSON, and_
from sqlalchemy.orm import mapped_column, Mapped, Session
from models.base_model import BaseModel
logger = logging.getLogger(__name__)


class CompetitionTablePromotionModel(BaseModel):
	__tablename__ = 'sport_competition_table_promotion'
	competition_id: Mapped[int] = mapped_column(Integer, primary_key=True)
	season_id:Mapped[int] = mapped_column(Integer, primary_key=True)
	promotion_id:Mapped[int] = mapped_column(Integer, primary_key=True)
	name_zh:Mapped[str] = mapped_column(String,nullable=False)
	name_zht:Mapped[str] = mapped_column(String,nullable=False)
	name_en:Mapped[str] = mapped_column(String,nullable=False)
	color:Mapped[str] = mapped_column(String,nullable=False)
	updated_at:Mapped[int] = mapped_column(Integer,nullable=False,default=time.time())

	def insert(self, session: Session):
		self.save(session)
		logger.info(f"sport_competition_table_promotion: 新增数据1条")