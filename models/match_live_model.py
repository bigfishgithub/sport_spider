import logging

from sqlalchemy import Integer, String, JSON, and_
from sqlalchemy.orm import Mapped, mapped_column, Session
from models.base_model import BaseModel

logger = logging.getLogger(__name__)
class MatchLiveModel(BaseModel):
    __tablename__ = 'sport_match_live'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tlive:Mapped[list] = mapped_column(JSON,default=[])
    score:Mapped[list] = mapped_column(JSON,default=[])
    stats: Mapped[list] = mapped_column(JSON,default=[])
    incidents:Mapped[list] = mapped_column(JSON,default=[])

    def insert(self, session: Session):
        self.save(session)
        logger.info(f"sport_match_live: 新增数据1条")

