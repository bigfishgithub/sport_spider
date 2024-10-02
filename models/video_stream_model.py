import logging
from sqlalchemy import Integer, String
from models.base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, Session

logger = logging.getLogger(__name__)


class VideoStreamModel(BaseModel):
	__tablename__ = 'sport_video_stream'
	match_id: Mapped[int] = mapped_column(Integer, primary_key=True)
	type:Mapped[int] = mapped_column(Integer, nullable=False,default=0)
	title:Mapped[str] = mapped_column(String(50), nullable=False)
	mobile_link:Mapped[str] = mapped_column(String(255), nullable=False,default=None)
	pc_link:Mapped[str] = mapped_column(String(255), nullable=False,default=None)
	cover:Mapped[str] = mapped_column(String(255), nullable=False,default=None)
	duration:Mapped[str] = mapped_column(String(255), nullable=False,default=0)

	def insert(self, session: Session):
		self.save(session)
		logger.info(f"sport_video_stream: 新增数据1条")

