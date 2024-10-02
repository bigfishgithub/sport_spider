import logging

from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column, Session

from models.base_model import BaseModel

logger = logging.getLogger(__name__)

class CompetitionPlayerStatsModel(BaseModel):
	__tablename__ = 'sport_competition_player_stats'
	competition_id:Mapped[int] = mapped_column(Integer,primary_key=True)
	season_id:Mapped[int] = mapped_column(Integer,primary_key=True)
	team_id:Mapped[int] = mapped_column(Integer,primary_key=True)
	player_id:Mapped[int] = mapped_column(Integer,primary_key=True)
	matches:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	court:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	first:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	goals:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	penalty:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	assists:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	minutes_played:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	red_cards:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	yellow_cards:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	yellow2red_cards:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	shots:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	shots_on_target:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	dribble:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	dribble_succ:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	clearances:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	blocked_shots:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	interceptions:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	tackles:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	passes:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	passes_accuracy:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	key_passes:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	crosses:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	crosses_accuracy:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	long_balls:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	long_balls_accuracy:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	duels:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	duels_won:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	dispossessed:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	fouls:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	was_fouled:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	offsides:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	saves:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	punches:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	runs_out:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	runs_out_succ:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	good_high_claim:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	freekicks:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	freekick_goals:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	hit_woodwork:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	fastbreaks:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	fastbreak_shots:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	fastbreak_goals:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	poss_losts:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
	rating:Mapped[int] = mapped_column(Integer,nullable=False,default=0)

	def insert(self, session: Session):
		self.save(session)
		logger.info(f"sport_competition_player_stats: 新增数据1条")


