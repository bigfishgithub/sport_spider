import asyncio
import logging
from concurrent.futures import ThreadPoolExecutor

from database import Database
from models.competition_list_model import CompetitionListModel

logger = logging.getLogger(__name__)
executor = ThreadPoolExecutor()
async def competition_detail_fetch():
	db = Database()
	session = db.get_session()  # 假设这是一个同步的 session
	loop = asyncio.get_running_loop()  # 获取当前事件循环
	try:
		# 使用 run_in_executor 将同步的数据库操作移到线程池中运行
		competition_ids = await loop.run_in_executor(executor, CompetitionListModel.get_edge_ids, session, 0)
		yield competition_ids
	except Exception as e:
		logger.error(e)
	finally:
		session.close()



