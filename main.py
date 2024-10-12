import asyncio
from datetime import datetime, date

from api.compesation_list import compesation_list_fetch
from api.competition_detail import competition_detail_fetch
from api.competition_list import competition_list_fetch
from api.coach_list import coach_list_fetch
from api.competition_rule_list import competition_rule_list_fetch
from api.delete_data import delete_data_fetch
from api.honor_list import honor_list_fetch
from api.live_stream import live_stream_fetch
from api.match_list import match_list_fetch
from api.match_live import match_live_fetch
from api.match_live_update import match_live_update_fetch
from api.match_trend import match_trend_fetch
from api.more_update import more_update_fetch
from api.player_list import player_list_fetch
from api.player_stats import player_stats_fetch
from api.player_stats_update import player_status_update_fetch
from api.referee_list import referee_list_fetch
from api.season_list import season_list_fetch
from api.stage_list import stage_list_fetch
from api.table_detail import table_detail_fetch
from api.team_list import team_list_fetch
from api.team_stats import team_stats_fetch
from api.team_stats_update import team_stats_update_fetch
from api.venue_list import venue_list_fetch
from get_all_data import init_data

from jobs.coach_job import CoachJob
from jobs.compensationList_job import CompensationListJob
from jobs.competition_job import CompetitionJob
from jobs.competition_rule_list_job import CompetitionRuleListJob
from jobs.competition_table_detail_job import  CompetitionTableDetailJob
from jobs.deleted_job import DeleteJob
from jobs.honor_list_job import HonorListJob
from jobs.live_stream_job import LiveStreamJob
from jobs.match_list_job import MatchListJob
from jobs.match_live_job import MatchLiveJob
from jobs.match_live_update_job import MatchLiveUpdateJob
from jobs.match_trend_job import MatchTrendJob
from jobs.more_update_job import MoreUpdateJob
from jobs.player_list_job import PlayerListJob
from jobs.player_stats_job import PlayerStatsJob
from jobs.player_stats_update_job import PlayerStatsUpdateJob
from jobs.referee_list_job import RefereeListJob
from jobs.season_list_job import SeasonListJob
from jobs.stage_list_job import StageListJob
from jobs.table_detail_job import TableDetailJob
from jobs.team_list_job import TeamListJob
from jobs.team_stats_job import TeamStatsJob
from jobs.team_stats_update_job import TeamStatsUpdateJob
from jobs.venue_list_job import VenueListJob
from logger import Logger
from process.producer import Producer  # 确保导入 Producer 类
from process.consumer import Consumer
from database import Database
from task_manager import TaskManager
import logging

Logger.setup_logging()

# 配置日志
logger = logging.getLogger(__name__)

# 初始化数据库
database = Database()
database.init_db()

# 创建任务管理器
task_manager = TaskManager()


async def run_producer_and_consumer(task_config):
	producer_tasks = []
	consumer_tasks = []

	for config in task_config:
		processing_done_event = asyncio.Event()

		# 创建生产者任务
		producer = Producer(config['func'], config['interval'], config['identifier'], processing_done_event)
		producer_tasks.append(asyncio.create_task(producer.produce()))

		# 创建消费者任务
		consumer = Consumer(config['process_func'], processing_done_event, config['identifier'])
		consumer_tasks.append(asyncio.create_task(consumer.consume()))

	# 等待所有生产者和消费者任务完成
	await asyncio.gather(*producer_tasks, *consumer_tasks)

	return producer_tasks, consumer_tasks


async def main():
	task_config = [
		# 任务配置
		{'func': player_list_fetch, 'interval': 30, 'identifier': 'player_list', 'process_func': PlayerListJob.run},
		{'func': match_trend_fetch, 'interval': 1, 'identifier': 'match_trend', 'process_func': MatchTrendJob.run},
		{'func': coach_list_fetch, 'interval': 60, 'identifier': 'coach_list', 'process_func': CoachJob.run},
		{'func': match_list_fetch, 'interval': 1, 'identifier': 'match_list', 'process_func': MatchListJob.run},
		{'func': team_list_fetch, 'interval': 1, 'identifier': 'team_list', 'process_func': TeamListJob.run},
		{'func': competition_list_fetch, 'interval': 60, 'identifier': 'competition_list','process_func': CompetitionJob.run},
		{'func': competition_rule_list_fetch, 'interval': 60, 'identifier': 'competition_rule_list','process_func': CompetitionRuleListJob.run},
		{'func': delete_data_fetch, 'interval': 60, 'identifier': 'delete_data', 'process_func': DeleteJob.run},
		{'func': honor_list_fetch, 'interval': 60, 'identifier': 'honor_list', 'process_func': HonorListJob.run},
		{'func': live_stream_fetch, 'interval': 10 * 60, 'identifier': 'live_stream', 'process_func': LiveStreamJob.run},
		{'func': match_live_fetch, 'interval': 1, 'identifier': 'match_live', 'process_func': MatchLiveJob.run},
		{'func': match_live_update_fetch, 'interval': 5, 'identifier': 'match_live_update', 'process_func': MatchLiveUpdateJob.run},
		{'func': more_update_fetch, 'interval': 20, 'identifier': 'more_update', 'process_func': MoreUpdateJob.run},
		{'func': player_stats_fetch, 'interval': 60, 'identifier': 'player_status', 'process_func': PlayerStatsJob.run},
		{'func': player_status_update_fetch, 'interval': 1, 'identifier': 'player_status_update','process_func': PlayerStatsUpdateJob.run},
		{'func': referee_list_fetch, 'interval': 60, 'identifier': 'referee_list', 'process_func': RefereeListJob.run},
		{'func': season_list_fetch, 'interval': 60, 'identifier': 'season_list', 'process_func': SeasonListJob.run},
		{'func': stage_list_fetch, 'interval': 60, 'identifier': 'stage_list', 'process_func': StageListJob.run},
		{'func': table_detail_fetch, 'interval': 60, 'identifier': 'table_detail', 'process_func': TableDetailJob.run},
		{'func': team_stats_fetch, 'interval': 60, 'identifier': 'team_stats', 'process_func': TeamStatsJob.run},
		{'func': team_stats_update_fetch, 'interval': 1, 'identifier': 'team_stats_update', 'process_func': TeamStatsUpdateJob.run},
		{'func': venue_list_fetch, 'interval': 60, 'identifier': 'venue_list', 'process_func': VenueListJob.run},
		{'func': compesation_list_fetch, 'interval': 60, 'identifier': 'compesation_list', 'process_func': CompensationListJob.run},
		{'func': competition_detail_fetch, 'interval': 1, 'identifier': 'competition_detail',
		 'process_func': CompetitionTableDetailJob.run},
	]

	try:

		# 	初始化全量数据
		await init_data()
		# 创建并运行生产者和消费者任务
		producer_tasks, consumer_tasks = await run_producer_and_consumer(task_config)

		# 等待所有消费者任务完成
		await asyncio.gather(*consumer_tasks, task_manager.run())
	except KeyboardInterrupt:
		logger.info("Interrupted by user, shutting down gracefully...")
	except Exception as e:
		logger.error(f"An error occurred: {e}")



if __name__ == "__main__":
	asyncio.run(main())

# async def main():
# 	db = Database()
# 	session = db.get_session()
# 	try:
# 		competition_ids = CompetitionListModel.get_edge_ids(session, 0)
# 		await CompetitionTableDetailJob.run(competition_ids)
# 		session.close()
# 	except Exception as e:
# 		logger.error(e)
# 	finally:
# 		session.close()
#
# if __name__ == '__main__':
# 	asyncio.run(main())
