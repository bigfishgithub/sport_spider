import logging
from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped, Session

from models.base_model import BaseModel

logger = logging.getLogger(__name__)


class CoachModel(BaseModel):
	__tablename__ = 'sport_coach'

	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	name_zh: Mapped[str] = mapped_column(String(50), nullable=False)
	name_en: Mapped[str] = mapped_column(String(50), nullable=False)
	name_zht: Mapped[str] = mapped_column(String(50), nullable=False)
	logo: Mapped[str] = mapped_column(String(255), nullable=False)
	birthday: Mapped[int] = mapped_column(Integer, nullable=False)
	age: Mapped[int] = mapped_column(Integer, nullable=False)
	preferred_formation: Mapped[str] = mapped_column(String(50))
	country_id: Mapped[int] = mapped_column(Integer, nullable=False)
	nationality: Mapped[str] = mapped_column(String(50))
	team_id: Mapped[int] = mapped_column(Integer, nullable=False)
	joined: Mapped[int] = mapped_column(Integer, nullable=False)
	contract_until: Mapped[int] = mapped_column(Integer, nullable=False)
	updated_at: Mapped[int] = mapped_column(Integer, nullable=False)

	@classmethod
	def insert(cls, session: Session,data_list):
		cls.save_all(session,data_list)
		logger.info(f"sport_coach: 新增数据{len(data_list)}条")
