import logging

from sqlalchemy import Integer, String, JSON, and_
from sqlalchemy.orm import Mapped, mapped_column, Session
from models.base_model import BaseModel

logger = logging.getLogger(__name__)
class MatchTrendModel(BaseModel):
    __tablename__ = 'sport_match_trend'

    match_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    count: Mapped[int] = mapped_column(Integer, nullable=False,default=0)
    per: Mapped[int] = mapped_column(Integer, nullable=False,default=0)
    data:Mapped[list] = mapped_column(JSON,default=[])
    incidents:Mapped[list] = mapped_column(JSON,default=[])
    full_data:Mapped[int] = mapped_column(Integer, default=0)

    def insert(self, session: Session):
        self.save(session)
        logger.info(f"sport_match_trend: 新增数据1条")
