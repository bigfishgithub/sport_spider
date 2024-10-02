import logging

from sqlalchemy.ext.declarative import declarative_base
# 创建 Base 类
Base = declarative_base()
logger = logging.getLogger(__name__)


class BaseModel(Base):
	"""所有模型的基类"""
	__abstract__ = True

	@classmethod
	def save_all(cls,session,data_list):
		for data in data_list:
			# 假设 data 是一个模型实例
			session.merge(data)  # 合并数据
		session.commit()  # 提交事务

	def save(self, session):
		"""保存到数据库"""
		session.merge(self)
		session.commit()

	@classmethod
	def delete(cls, session,ids):
		"""从数据库中删除"""
		session.query(cls).filter(cls.id.in_(ids)).delete(synchronize_session=False)
		session.commit()



