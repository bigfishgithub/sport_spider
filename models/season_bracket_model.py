import logging

from sqlalchemy import Integer, JSON
from sqlalchemy.orm import Mapped, Session, mapped_column

from models.base_model import BaseModel

logger = logging.getLogger(__name__)

class SeasonBracketModel(BaseModel):
	__tablename__ = 'sport_season_bracket'
	seasion_id :Mapped[int] = mapped_column(Integer,primary_key=True)
	brackets:Mapped[list] = mapped_column(JSON,default=[])
	groups: Mapped[list] = mapped_column(JSON, default=[])
	rounds: Mapped[list] = mapped_column(JSON, default=[])
	match_ups: Mapped[list] = mapped_column(JSON, default=[])

	def insert(self, session: Session):
		self.save(session)
		logger.info(f"sport_match_lineup: 新增数据1条")
