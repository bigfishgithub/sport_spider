import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config

logger = logging.getLogger(__name__)

class Database:
    """数据库连接和会话管理类"""

    def __init__(self):
        try:
            # 初始化数据库引擎，设置连接池参数
            self.engine = create_engine(
                Config.DATABASE_ENGINE,
                echo=False,
                future=True,
                pool_size=560,  # 连接池中保持的连接数
                max_overflow=10,  # 超出连接池大小的最大连接数
                pool_timeout=30,  # 等待连接池连接的最长时间
                pool_recycle=1800  # 连接回收时间（秒）
            )
            self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
            logger.info("Database connection established.")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {str(e)}")
            raise

    def get_session(self):
        """获取数据库会话"""
        try:
            return self.SessionLocal()
        except Exception as e:
            logger.error(f"Unexpected error occurred while getting a session: {str(e)}")

    def init_db(self):
        """初始化数据库（创建表等）"""
        from models.base_model import Base
        Base.metadata.create_all(bind=self.engine)