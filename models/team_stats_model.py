import logging
from sqlalchemy import Integer, JSON
from models.base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, Session

logger = logging.getLogger(__name__)


class TeamStatsModel(BaseModel):
	__tablename__ = 'sport_team_stats'
	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	stats:Mapped[list] = mapped_column(JSON,default=[])

	def insert(self, session: Session):
		self.save(session)
		logger.info(f"sport_team_stats: 新增数据1条")

