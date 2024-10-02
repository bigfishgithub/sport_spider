import asyncio

data_queues = {}  # 存储每个接口的队列

def get_queue(identifier):
    if identifier not in data_queues:
        data_queues[identifier] = asyncio.Queue()
    return data_queues[identifier]

