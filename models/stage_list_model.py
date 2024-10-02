import logging

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, Session
from models.base_model import BaseModel

logger = logging.getLogger(__name__)
class StageListModel(BaseModel):
    __tablename__ = 'sport_stage'

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    season_id:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
    name_zh:Mapped[str] = mapped_column(String(50),nullable=False)
    name_zht:Mapped[str] = mapped_column(String(50),nullable=False)
    name_en:Mapped[str] = mapped_column(String(100),nullable=False)
    mode:Mapped[Integer] = mapped_column(Integer,nullable=False,default=0)
    group_count:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
    round_count:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
    order:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
    updated_at:Mapped[int] = mapped_column(Integer,nullable=False,default=0)

    def insert(self, session: Session):
        self.save(session)
        logger.info(f"sport_stage: 新增数据1条")