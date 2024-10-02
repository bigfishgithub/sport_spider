import logging
from sqlalchemy import Integer, String
from models.base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, Session

logger = logging.getLogger(__name__)


class LiveStreamModel(BaseModel):
	__tablename__ = 'sport_live_stream'

	match_id: Mapped[int] = mapped_column(Integer, primary_key=True)
	match_time: Mapped[int] = mapped_column(Integer, nullable=False)
	comp: Mapped[str] = mapped_column(String, nullable=False, default=None)
	home: Mapped[str] = mapped_column(String, nullable=False, default=None)
	away: Mapped[str] = mapped_column(String, nullable=False, default=None)
	pc_link: Mapped[str] = mapped_column(String,  default=None)
	mobile_link:Mapped[str] = mapped_column(String, default=None)

	def insert(self, session: Session):
		self.save(session)
		logger.info(f"sport_live_stream: 新增数据1条")
