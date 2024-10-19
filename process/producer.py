import asyncio
import logging
from asyncio import create_task

from process.consumer import Consumer
from process.queue import get_queue
from math import ceil
# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 生产者类
class Producer:
    def __init__(self, func, interval, identifier,process_funcs,batch_size=100,max_consumers=20):
        self.func = func
        self.interval = interval
        self.identifier = identifier
        self.queue = get_queue(identifier)
        self.process_funcs = process_funcs
        self.batch_size = batch_size
        self.max_consumers = max_consumers

    async def produce(self):
        while True:
            try:

                async for data in self.func():
                    if not data:
                        logger.info(f"No results for {self.identifier}, skipping...")
                        continue

                    if isinstance(data, list):
                        batch_data = data
                    else:
                        batch_data = [data]
                        print(batch_data)
                    await self._dispatch_to_consumers(batch_data)
                    batch_data.clear()


                # 每次循环后等待设定的时间间隔
                await asyncio.sleep(self.interval)

            except Exception as e:
                logger.error(f"Error in producing data for {self.identifier}: {e}")

    async def _dispatch_to_consumers(self, batch_data):
        """
        分发数据到消费者任务
        """
        # 根据队列大小计算需要多少消费者
        data_len = ceil(len(batch_data) / self.batch_size)

        consumers = []
        for i in range(data_len):
            start = i * self.batch_size
            end = (i + 1) * self.batch_size
            sub_batch = batch_data[start:end]
            customer = Consumer(self.process_funcs, self.identifier,sub_batch)
            consumers.append(asyncio.create_task(customer.consume()))

        # 使用 gather 并发运行消费者任务
        await asyncio.gather(*consumers)


