import logging
import time

from sqlalchemy import Integer, String, JSON, and_
from sqlalchemy.orm import mapped_column, Mapped, Session
from models.base_model import BaseModel
logger = logging.getLogger(__name__)


class CompetitionTableDetailModel(BaseModel):
	__tablename__ = 'sport_competition_table_detail'

	competition_id: Mapped[int] = mapped_column(Integer, primary_key=True)
	season_id: Mapped[int] = mapped_column(Integer, primary_key=True)
	table_id: Mapped[int] = mapped_column(Integer, primary_key=True)
	team_id: Mapped[int] = mapped_column(Integer, primary_key=True)
	conference: Mapped[str] = mapped_column(String,nullable=False,default=None)
	group: Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	stage_id:Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	promotion_id:Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	points:Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	position:Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	deduct_points:Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	note:Mapped[str] = mapped_column(String, nullable=False,default=None)
	total:Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	won:Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	draw:Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	loss:Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	goals:Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	goals_against:Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	goal_diff:Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	home_points:Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	home_position:Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	home_total:Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	home_won:Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	home_draw:Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	home_loss:Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	home_goals:Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	home_goals_against:Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	home_goal_diff:Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	away_points:Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	away_position:Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	away_total:Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	away_won:Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	away_draw:Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	away_loss:Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	away_goals:Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	away_goals_against:Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	away_goal_diff:Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	updated_at:Mapped[int] = mapped_column(Integer, nullable=False,default=time.time())

	def insert(self, session: Session):
		self.save(session)
		logger.info(f"sport_competition_table_detail: 新增数据1条")





