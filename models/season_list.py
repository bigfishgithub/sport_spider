import logging

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, Session
from models.base_model import BaseModel

logger = logging.getLogger(__name__)
class SeasonListModel(BaseModel):
    __tablename__ = 'sport_season'

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    competition_id:Mapped[int] = mapped_column(Integer,default=0)
    year:Mapped[str] = mapped_column(String(30),nullable=False)
    start_time:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
    end_time:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
    is_current:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
    has_player_stats:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
    has_team_stats:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
    has_table:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
    updated_at:Mapped[int] = mapped_column(Integer,nullable=False,default=0)

    def insert(self, session: Session):
        self.save(session)
        logger.info(f"sport_season: 新增数据1条")