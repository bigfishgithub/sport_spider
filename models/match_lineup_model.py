import logging

from sqlalchemy import Integer, String, JSON
from sqlalchemy.orm import Mapped, mapped_column, Session
from models.base_model import BaseModel

logger = logging.getLogger(__name__)
class MatchLineupModel(BaseModel):
    __tablename__ = 'sport_match_lineup'

    match_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    confirmed:Mapped[int] = mapped_column(Integer,nullable=False, default=0)
    home_formation:Mapped[str] = mapped_column(String, default=None)
    away_formation:Mapped[str] = mapped_column(String, default=None)
    home_color:Mapped[str] = mapped_column(String, default=None)
    away_color:Mapped[str] = mapped_column(String, default=None)
    away:Mapped[list] = mapped_column(JSON, default=[])
    home:Mapped[list] = mapped_column(JSON, default=[])
    has_name_en:Mapped[int] = mapped_column(Integer, default=0)

    def insert(self, session: Session):
        self.save(session)
        logger.info(f"sport_match_lineup: 新增数据1条")
