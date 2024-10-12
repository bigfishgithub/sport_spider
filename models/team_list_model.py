import logging
from sqlalchemy import Integer, String, SMALLINT
from models.base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, Session

logger = logging.getLogger(__name__)


class TeamListModel(BaseModel):
	__tablename__ = 'sport_team'
	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	competition_id: Mapped[int] = mapped_column(Integer, nullable=False)
	country_id: Mapped[int] = mapped_column(Integer, nullable=False)
	coach_id: Mapped[int] = mapped_column(Integer, nullable=False)
	name_zh: Mapped[str] = mapped_column(String(50), nullable=False)
	name_zht: Mapped[str] = mapped_column(String(50), nullable=False)
	name_en: Mapped[str] = mapped_column(String(100), nullable=False)
	name_vi: Mapped[str] = mapped_column(String(100), nullable=False, default='')
	short_name_zh: Mapped[str] = mapped_column(String(50), nullable=False)
	short_name_zht: Mapped[str] = mapped_column(String(50), nullable=False)
	short_name_en: Mapped[str] = mapped_column(String(100), nullable=False)
	logo: Mapped[str] = mapped_column(String(255), nullable=False)
	national: Mapped[int] = mapped_column(SMALLINT, nullable=False)
	country_logo: Mapped[str] = mapped_column(String(255), nullable=False)
	foundation_time: Mapped[int] = mapped_column(Integer, nullable=False)
	website: Mapped[str] = mapped_column(String(255))
	venue_id: Mapped[int] = mapped_column(Integer, nullable=False)
	market_value: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
	market_value_currency: Mapped[str] = mapped_column(String(20), default=None)
	total_players: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
	foreign_players: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
	national_players: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
	uid: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
	updated_at: Mapped[int] = mapped_column(Integer, nullable=False)

	def insert(self, session: Session):
		self.save(session)
		logger.info(f"sport_team: 新增数据1条")

	@classmethod
	def hasData(cls,session: Session,team_id):
		return session.query(cls).filter(cls.id == team_id).scalar()


