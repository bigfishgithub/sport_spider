import logging

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, Session
from models.base_model import BaseModel

logger = logging.getLogger(__name__)
class VenueListModel(BaseModel):
    __tablename__ = 'sport_venue'

    id:Mapped[str] = mapped_column(String(30), primary_key=True)
    name_zh:Mapped[str] = mapped_column(String(50),nullable=False)
    name_zht:Mapped[str] = mapped_column(String(50),nullable=False)
    name_en:Mapped[str] = mapped_column(String(100),nullable=False)
    capacity:Mapped[int] = mapped_column(Integer,nullable=False)
    country_id:Mapped[int] = mapped_column(Integer,nullable=False)
    updated_at:Mapped[int] = mapped_column(Integer,nullable=False)

    def insert(self, session: Session):
        self.save(session)
        logger.info(f"sport_venue: 新增数据1条")
