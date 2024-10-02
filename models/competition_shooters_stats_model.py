
import logging

from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column, Session

from models.base_model import BaseModel

logger = logging.getLogger(__name__)

class CompetitionShottersStatsModel(BaseModel):
	__tablename__ = 'sport_competition_shooters_stats'
	competition_id:Mapped[int] = mapped_column(Integer,primary_key=True)
	season_id:Mapped[int] = mapped_column(Integer,primary_key=True)
	team_id:Mapped[int] = mapped_column(Integer,primary_key=True)
	player_id:Mapped[int] = mapped_column(Integer,primary_key=True)
	position:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	goals:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	penalty:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	assists:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	minutes_played:Mapped[int] = mapped_column(Integer,nullable=False,default=0)

	def insert(self, session: Session):
		self.save(session)
		logger.info(f"sport_competition_shooters_stats: 新增数据1条")


