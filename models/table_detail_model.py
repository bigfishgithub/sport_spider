

import logging

from sqlalchemy import Integer, String, JSON
from sqlalchemy.orm import Mapped, mapped_column, Session
from models.base_model import BaseModel

logger = logging.getLogger(__name__)
class TableDetailModel(BaseModel):
    __tablename__ = 'sport_table_detail'

    competition_id:Mapped[int] = mapped_column(Integer, primary_key=True)
    season_id:Mapped[int] = mapped_column(Integer,nullable=False)
    promotions:Mapped[list] = mapped_column(JSON,default=[])
    tables:Mapped[list] = mapped_column(JSON,default=[])
    updated_at:Mapped[int] = mapped_column(Integer,nullable=False,default=0)

    def insert(self, session: Session):
        self.save(session)
        logger.info(f"sport_table_live: 新增数据1条")
