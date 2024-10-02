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
                async for data in self.func():
                    if not data:
                        logger.info(f"No results for {self.identifier}, skipping...")
                        continue

                    if isinstance(data, list):
                        for item in data:
                            await self.queue.put((self.identifier, item))
                    else:
                        await self.queue.put((self.identifier, data))

                # 等待消费者处理完
                await self.processing_done_event.wait()
                self.processing_done_event.clear()

                await asyncio.sleep(self.interval)
            except Exception as e:
                logger.error(f"Error in producing data for {self.identifier}: {e}")


