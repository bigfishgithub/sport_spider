import logging
from sqlalchemy import Integer, String, JSON, Index

from models.base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, Session

logger = logging.getLogger(__name__)


class PlayerListModel(BaseModel):
	__tablename__ = 'sport_player'

	__table_args__ = (
		Index('idx_updated_at', 'updated_at', mysql_length=255, mysql_using='BTREE', postgresql_using='BTREE'),
	)

	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	name_zh: Mapped[str] = mapped_column(String(50), nullable=False)
	name_zht: Mapped[str] = mapped_column(String(50), nullable=False)
	name_en: Mapped[str] = mapped_column(String(100), nullable=False)
	name_vi: Mapped[str] = mapped_column(String(100), nullable=False, default='')
	short_name_zh: Mapped[str] = mapped_column(String(50), nullable=False)
	short_name_zht: Mapped[str] = mapped_column(String(50), nullable=False)
	short_name_en: Mapped[str] = mapped_column(String(100), nullable=False)
	logo: Mapped[str] = mapped_column(String(255), nullable=False)
	country_id: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
	nationality: Mapped[str] = mapped_column(String(50), default=None)
	national_logo: Mapped[str] = mapped_column(String(255), default=None)
	birthday: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
	age: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
	height: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
	weight: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
	market_value: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
	market_value_currency: Mapped[int] = mapped_column(String(10), default=0)
	contract_until: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
	preferred_foot: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
	suffix: Mapped[str] = mapped_column(String(50), default='0', nullable=False)
	coach_id: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
	uid: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
	ability: Mapped[str] = mapped_column(JSON, nullable=False, default=0)
	characteristics: Mapped[str] = mapped_column(JSON, default=None)
	position: Mapped[str] = mapped_column(String(20), default=None)
	positions: Mapped[int] = mapped_column(JSON, default=None)
	updated_at: Mapped[int] = mapped_column(Integer, nullable=False)

	def insert(self, session):
		self.save(session)
		logger.info(f"sport_player: 新增数据1条")

	@classmethod
	def get_player(cls,session,id):
		return session.query(cls).filter(PlayerListModel.id == id).first()

