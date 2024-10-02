import logging

from models.base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, Session
from sqlalchemy import String, Integer, Text,JSON

logger = logging.getLogger(__name__)


class CompetitionRuleListModel(BaseModel):
	__tablename__ = 'sport_competition_rule'

	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	competition_id: Mapped[int] = mapped_column(Integer, nullable=False)
	season_ids: Mapped[str] = mapped_column(JSON, default=None)
	text: Mapped[str] = mapped_column(Text, default=None)
	updated_at: Mapped[int] = mapped_column(Integer, default=0)

	def insert(self, session: Session):
		self.save(session)
		logger.info(f"sport_competition_rule: 新增数据1条")

