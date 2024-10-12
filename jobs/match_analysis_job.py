import asyncio
import logging
from datetime import date, datetime

from api.football_apis import get_match_analysis
from database import Database
from models.match_analysis_model import MatchAlalysisModel
from models.match_list_model import MatchListModel

logger = logging.getLogger(__name__)


class MatchAnalysisJob:

	@classmethod
	async def run(cls):

		# 获取未开赛30天的数据
		time = 60 * 60 * 24 * 30
		today = date.today()
		dt = datetime.combine(today, datetime.min.time())

		# 获取时间戳
		now = int(dt.timestamp())
		session = None
		ids = []
		try:
			db = Database()
			session = db.get_session()
			ids = MatchListModel.get_30dyas_date_ids(session, now, now + time)
		except Exception as e:
			logger.error(e)
		finally:
			if session: session.close()
		queue = asyncio.Queue()
		for id_value in ids:
			queue.put_nowait(id_value[0])


		# 创建多个并发任务处理队列中的数据
		workers = [asyncio.create_task(cls.worker(queue)) for _ in range(50)]  # 启动50个工作协程
		await queue.join()  # 等待所有任务完成

		# 停止工作协程
		for _ in workers:
			await queue.put(None)  # 向队列中放入结束信号
		await asyncio.gather(*workers)  # 等待所有工作协程完成

	@classmethod
	async def worker(cls, queue):
		"""工作协程：从队列中获取数据并处理"""
		while True:
			match_id = await queue.get()  # 从队列中获取match_id
			if match_id is None:  # 使用None作为结束信号
				break
			response = await get_match_analysis({"id": match_id})
			if response['results']:
				data = response['results']
				data['match_id'] = match_id
				session = None
				try:
					db = Database()
					session = db.get_session()
					match_analysis = MatchAlalysisModel(**data)
					match_analysis.insert(session)
				except Exception as e:
					if session: session.rollback()
					logger.error(e)
				finally:
					if session: session.close()
			queue.task_done()  # 标记该任务已完成
