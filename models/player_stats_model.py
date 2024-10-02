from sqlalchemy import Integer, String, JSON
from sqlalchemy.orm import mapped_column, Session, Mapped
import logging
from models.base_model import BaseModel

logger = logging.getLogger(__name__)


class PlayerStatsModel(BaseModel):
	__tablename__ = 'sport_player_stats'
	match_id: Mapped[int] = mapped_column(Integer, primary_key=True)
	player_stats: Mapped[list] = mapped_column(JSON, default=[])

	def insert(self, session: Session):
		self.save(session)
		logger.info(f"sport_player_stats: 新增数据1条")

