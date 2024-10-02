import asyncio

from process.queue import get_queue
import logging

logger = logging.getLogger(__name__)


class Consumer:
    def __init__(self, process_funcs, processing_done_event, identifier):
        self.process_funcs = process_funcs
        self.processing_done_event = processing_done_event
        self.identifier = identifier
        self.queue = get_queue(identifier)

    async def consume(self):
        while True:
            batch = []
            id = None
            while not self.queue.empty():
                try:
                    id, data = await self.queue.get()
                    if not data:
                        logger.warning(f"Data for {id} is not a recognized format, skipping...")
                        continue
                    batch.append(data)
                    self.queue.task_done()
                except asyncio.QueueEmpty:
                    break

            if id is not None and id in self.process_funcs and batch:
                try:
                    await self.process_funcs[id](batch)
                except Exception as e:
                    logger.error(f"Error processing data for {id}: {e}")

            # 通知生产者当前消费任务完成
            self.processing_done_event.set()

            # 等待生产者的确认
            await self.processing_done_event.wait()
            self.processing_done_event.clear()

            await asyncio.sleep(0)

