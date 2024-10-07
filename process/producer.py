import asyncio
import logging

from process.queue import get_queue

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 生产者类
class Producer:
    def __init__(self, func, interval, identifier, processing_done_event):
        self.func = func
        self.interval = interval
        self.identifier = identifier
        self.processing_done_event = processing_done_event
        self.queue = get_queue(identifier)

    async def produce(self):
        while True:
            try:
                has_data = False  # 添加标记，判断当前是否有数据需要处理

                async for data in self.func():
                    if not data:
                        logger.info(f"No results for {self.identifier}, skipping...")
                        continue

                    has_data = True  # 有数据时，设置标记为True

                    if isinstance(data, list):
                        for item in data:
                            await self.queue.put((self.identifier, item))
                    else:
                        await self.queue.put((self.identifier, data))

                if has_data:
                    # 如果有数据，等待消费者处理完
                    await self.processing_done_event.wait()
                    self.processing_done_event.clear()
                else:
                    # 如果没有数据，直接等待下一个周期
                    logger.info(f"No data to process for {self.identifier}, waiting for the next interval...")

                # 每次循环后等待设定的时间间隔
                await asyncio.sleep(self.interval)

            except Exception as e:
                logger.error(f"Error in producing data for {self.identifier}: {e}")


