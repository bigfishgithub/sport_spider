import logging

from sqlalchemy import Integer, JSON
from sqlalchemy.orm import Mapped, mapped_column, Session
from models.base_model import BaseModel

logger = logging.getLogger(__name__)
class MatchAlalysisModel(BaseModel):
    __tablename__ = 'sport_match_analysis'

    match_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    info: Mapped[dict] = mapped_column(JSON)
    history:Mapped[dict] = mapped_column(JSON)
    future:Mapped[dict] = mapped_column(JSON)
    goal_distribution:Mapped[dict] = mapped_column(JSON)

    def insert(self, session: Session):
        self.save(session)
        logger.info(f"sport_match_analysis: 新增数据1条")