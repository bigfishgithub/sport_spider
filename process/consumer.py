import asyncio

from models.match_list_model import MatchListModel
import logging

from utils import Utils

logger = logging.getLogger(__name__)


class Consumer:
    def __init__(self, process_funcs, identifier,data):
        self.process_funcs = process_funcs
        self.identifier = identifier
        self.data = data

    async def consume(self):
        # 创建 20 个并发工作任务
        try:
            if not self.data:
                logger.warning(f"Data for {self.identifier} is not a recognized format, skipping...")
                # 设置超时，例如5秒
            # for item in self.data:
            #     print(item)
            #     await asyncio.wait_for(self.process_funcs(item), 60)

        except asyncio.TimeoutError:
            logger.warning(f"Processing for {self.data} timed out.")
        except Exception as e:
            logger.error(f"Error processing data for: {e}")
        finally:
            pass
            # update_list = ['player_list', 'match_list', 'coach_list', 'competition_list',
            #                'competition_rule_list', 'honor_list', 'referee_list',
            #                'season_list', 'venue_list', 'compensation_list']
            # if self.identifier in update_list:
            #     Utils.update_last_data(MatchListModel, self.identifier)




