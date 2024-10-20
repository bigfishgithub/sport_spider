import logging

from sqlalchemy import Integer, String, JSON, and_, or_
from sqlalchemy.orm import Mapped, mapped_column, Session

from database import Database
from models.base_model import BaseModel
from enums.match_type import MatchType

logger = logging.getLogger(__name__)


class MatchListModel(BaseModel):
	__tablename__ = 'sport_match'

	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	season_id: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
	competition_id: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
	home_team_id: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
	away_team_id: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
	status_id: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
	match_time: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
	venue_id: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
	referee_id: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
	related_id: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
	neutral: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
	note: Mapped[str] = mapped_column(String, default=None)
	home_scores: Mapped[dict] = mapped_column(JSON, default={})
	away_scores: Mapped[dict] = mapped_column(JSON, default={})
	home_position: Mapped[str] = mapped_column(String, default=None)
	away_position: Mapped[str] = mapped_column(String, default=None)
	coverage: Mapped[dict] = mapped_column(JSON, default={})
	agg_score: Mapped[dict] = mapped_column(JSON, default={})
	environment: Mapped[dict] = mapped_column(JSON, nullable=True, default={})
	round: Mapped[str] = mapped_column(JSON, default={})
	updated_at: Mapped[int] = mapped_column(Integer, default=0)

	def insert(self, session: Session):
		self.save(session)
		logger.info(f"sport_match: 新增数据1条")

	@classmethod
	def get_30dyas_date_ids(cls, session, min_time, max_time):
		return session.query(cls.id).filter(and_(cls.match_time >= int(min_time), cls.match_time <= int(max_time))).all()
