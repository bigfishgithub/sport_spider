import logging

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, Session
from models.base_model import BaseModel

logger = logging.getLogger(__name__)
class HonorListModel(BaseModel):
    __tablename__ = 'sport_honor'

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    name_zh:Mapped[str] = mapped_column(String(50), nullable=False)
    name_zht:Mapped[str] = mapped_column(String(50), nullable=False)
    name_en:Mapped[str] = mapped_column(String(100), nullable=False,default='')
    logo:Mapped[str] = mapped_column(String(255), nullable=False)
    updated_at:Mapped[int] = mapped_column(Integer,nullable=False,default=0)

    def insert(self, session: Session):
        self.save(session)
        logger.info(f"sport_honor: 新增数据1条")