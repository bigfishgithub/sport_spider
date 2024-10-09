import asyncio

from models.match_list_model import MatchListModel
from process.queue import get_queue
import logging

from utils import Utils

logger = logging.getLogger(__name__)


class Consumer:
	def __init__(self, process_funcs, processing_done_event, identifier):
		self.process_funcs = process_funcs
		self.processing_done_event = processing_done_event
		self.identifier = identifier
		self.queue = get_queue(identifier)

	async def consume(self):
		# 创建 10 个并发工作任务
		workers = [asyncio.create_task(self.worker()) for _ in range(20)]
		await asyncio.gather(*workers)  # 等待所有工作协程完成

	async def worker(self):
		while True:
			try:
				data = await self.queue.get()  # 从队列中获取数据
				if data is None:  # 检查结束信号
					break

				if not data:
					logger.warning(f"Data for {self.identifier} is not a recognized format, skipping...")
					continue
				await self.process_funcs(data[1])
				self.queue.task_done()

			except Exception as e:
				logger.error(f"Error processing data for: {e}")

			finally:
				update_list = ['player_list', 'match_list', 'coach_list', 'competition_list', 'competition_rule_list',
				               'honor_list', 'referee_list', 'season_list', 'venue_list', 'compensation_list']
				if self.identifier in update_list:
					Utils.update_last_data(MatchListModel, self.identifier)

				# 当所有数据处理完时，通知生产者
				if self.queue.empty():
					self.processing_done_event.set()
