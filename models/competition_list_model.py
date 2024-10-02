import logging
from sqlalchemy import Integer, String, JSON
from sqlalchemy.orm import mapped_column, Mapped, Session
from models.base_model import BaseModel

logger = logging.getLogger(__name__)


class CompetitionListModel(BaseModel):
	__tablename__ = 'sport_competition'

	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	country_id: Mapped[int] = mapped_column(Integer, nullable=False)
	category_id: Mapped[int] = mapped_column(Integer, nullable=False)
	name_zh: Mapped[str] = mapped_column(String(50), nullable=False)
	name_zht: Mapped[str] = mapped_column(String(50), nullable=False)
	name_en: Mapped[str] = mapped_column(String(100), nullable=False)
	name_vi: Mapped[str] = mapped_column(String(100), nullable=False, default='')
	short_name_zh: Mapped[str] = mapped_column(String(50), nullable=False)
	short_name_zht: Mapped[str] = mapped_column(String(50), nullable=False)
	short_name_en: Mapped[str] = mapped_column(String(100), nullable=False)
	logo: Mapped[str] = mapped_column(String(255), nullable=False)
	type: Mapped[int] = mapped_column(Integer, nullable=False)
	title_holder: Mapped[str] = mapped_column(JSON)
	most_titles: Mapped[str] = mapped_column(JSON)
	newcomers: Mapped[str] = mapped_column(JSON)
	divisions: Mapped[str] = mapped_column(JSON)
	host: Mapped[str] = mapped_column(JSON)
	primary_color: Mapped[str] = mapped_column(String(255))
	secondary_color: Mapped[str] = mapped_column(String(255))
	updated_at: Mapped[int] = mapped_column(Integer, nullable=False)

	def insert(self, session: Session):
		self.save(session)
		logger.info(f"sport_competition: 新增数据1条")


