import asyncio
import logging
import time
from datetime import date, datetime

from api.football_apis import get_competition_list, get_competition_rule_list, get_honor_list, get_match_list, \
	get_team_list, get_venue_list, get_player_list, get_coach, get_referee_list, get_season_list, get_stage_list, \
	get_compensation_list
from database import Database
from jobs.category_job import CategoryJob
from jobs.coach_job import CoachJob
from jobs.compensationList_job import CompensationListJob
from jobs.competition_job import CompetitionJob
from jobs.competition_rule_list_job import CompetitionRuleListJob
from jobs.country_job import CountryJob
from jobs.honor_list_job import HonorListJob
from jobs.match_analysis_job import MatchAnalysisJob
from jobs.match_list_job import MatchListJob
from jobs.match_trend_job import MatchTrendJob
from jobs.player_list_job import PlayerListJob
from jobs.referee_list_job import RefereeListJob
from jobs.season_list_job import SeasonListJob
from jobs.stage_list_job import StageListJob
from jobs.team_list_job import TeamListJob
from jobs.venue_list_job import VenueListJob
from models.match_list_model import MatchListModel
from utils import Utils

logger = logging.getLogger(__name__)


async def init_player_list():
	params = {"id": -1, "limit": 1000, "time": 0}
	last_fetch = Utils.get_state_data("player_list")
	if last_fetch.max_time == 0:
		is_true = True
		while is_true:
			try:
				last_fetch = Utils.get_state_data("player_list")
				params['id'] = last_fetch.max_id
				params['limit'] = last_fetch.limit
				response = await get_player_list(params)
				if response['results']:
					await PlayerListJob.run(response['results'])
				else:
					last_fetch = Utils.get_state_data("player_list")
					params['id'] = -1
					params['time'] = last_fetch.max_time
					params['limit'] = last_fetch.limit
					response = await get_player_list(params)
					if response['results']:
						for item in response['results']:
							await PlayerListJob.run(item)
						Utils.update_last_data(MatchListModel, 'player_list')
					else:
						is_true = False

			except Exception as e:
				logger.error(e)


async def init_competition_list():
	params = {"id": -1, "limit": 1000, "time": 0}
	last_fetch = Utils.get_state_data('competition_list')
	if last_fetch.max_time == 0:
		is_true = True
		while is_true:
			try:
				last_fetch = Utils.get_state_data('competition_list')
				params['id'] = last_fetch.max_id
				params['limit'] = last_fetch.limit
				response = await get_competition_list(params)
				if response['results']:
					for item in response['results']:
						await CompetitionJob.run(item)
					Utils.update_last_data(MatchListModel, 'competition_list')
				else:
					is_true = False
			except Exception as e:
				logger.error(e)


async def init_competition_rule():
	params = {"id": -1, "limit": 1000, "time": 0}
	last_fetch = Utils.get_state_data("competition_rule_list")
	if last_fetch.max_time == 0:
		is_true = True
		while is_true:
			try:
				last_fetch = Utils.get_state_data("competition_rule_list")
				params['id'] = last_fetch.max_id
				params['limit'] = last_fetch.limit
				response = await get_competition_rule_list(params)
				if response['results']:
					for item in response['results']:
						await CompetitionRuleListJob.run(item)
					Utils.update_last_data(MatchListModel, 'competition_rule_list')
				else:
					is_true = False
			except Exception as e:
				logger.error(f"live_stream请求错误：{e}")


async def init_honor_list():
	params = {"id": -1, "limit": 1000, "time": 0}
	last_fetch = Utils.get_state_data("honor_list")
	if last_fetch.max_time == 0:
		is_true = True
		while is_true:
			try:
				last_fetch = Utils.get_state_data("honor_list")
				params['id'] = int(last_fetch.max_id)
				params['limit'] = last_fetch.limit
				response = await get_honor_list(params)
				if response['results']:
					for item in response['results']:
						await HonorListJob.run(item)
					Utils.update_last_data(MatchListModel, 'honor_list')
				else:
					is_true = False
			except Exception as e:
				logger.error(f"live_stream请求错误：{e}")


async def init_match_list():
	params = {"id": -1, "limit": 1000, "time": 0}
	is_true = True
	last_fetch = Utils.get_state_data("match_list")
	if last_fetch.max_time == 0:
		while is_true:
			try:
				last_fetch = Utils.get_state_data("match_list")
				params['id'] = int(last_fetch.max_id)
				params['limit'] = last_fetch.limit
				response = await get_match_list(params)
				if response['results']:
					for item in response['results']:
						await MatchListJob.run(item)
					Utils.update_last_data(MatchListModel, 'match_list')
				else:
					is_true = False
			except Exception as e:
				logging.error(f"match_list_fetch: {e}")


async def init_team_list():
	params = {"id": -1, "limit": 100, "time": 0}
	last_fetch = Utils.get_state_data("team_list")
	if last_fetch.max_time == 0:
		is_true = True
		while is_true:
			last_fetch = Utils.get_state_data("team_list")
			params['id'] = last_fetch.max_id
			params['limit'] = last_fetch.limit
			response = await get_team_list(params)
			if response['results']:
				for item in response['results']:
					await TeamListJob.run(item)
				Utils.update_last_data(MatchListModel, 'team_list')
			else:
				is_true = False


async def init_venue_list():
	params = {"id": -1, "limit": 1000, "time": 0}
	last_fetch = Utils.get_state_data("venue_list")
	if last_fetch.max_time == 0:
		is_true = True
		while is_true:
			try:
				last_fetch = Utils.get_state_data("venue_list")
				params['id'] = int(last_fetch.max_id)
				params['limit'] = last_fetch.limit
				response = await get_venue_list(params)
				if response['results']:
					for item in response['results']:
						await VenueListJob.run(item)
					Utils.update_last_data(MatchListModel, 'venue_list')
				else:
					is_true = False
			except Exception as e:
				logger.error(e)


async def init_coach_list():
	params = {"id": -1, "limit": 1000, "time": 0}
	last_fetch = Utils.get_state_data("coach_list")
	if last_fetch.max_time == 0:
		is_true = True
		while is_true:
			try:
				last_fetch = Utils.get_state_data("coach_list")
				params['id'] = last_fetch.max_id
				params['limit'] = last_fetch.limit
				response = await get_coach(params)
				if response['results']:
					for item in response['results']:
						await CoachJob.run(item)
					Utils.update_last_data(MatchListModel, 'coach_list')
				else:
					is_true = False
			except Exception as e:
				logger.error(f"coach_list_fetch:{e}")


async def init_feree_list():
	params = {"id": -1, "limit": 1000, "time": 0}
	last_fetch = Utils.get_state_data("referee_list")
	if not last_fetch or last_fetch.max_time == 0:
		is_true = True
		while is_true:
			try:
				last_fetch = Utils.get_state_data("referee_list")
				params['id'] = last_fetch.max_id
				params['limit'] = last_fetch.limit
				response = await get_referee_list(params)
				if response['results']:
					for item in response['results']:
						await RefereeListJob.run(item)
					Utils.update_last_data(MatchListModel, 'referee_list')
				else:
					is_true = False
			except Exception as e:
				logger.error(e)


async def init_season_list():
	params = {"id": -1, "limit": 1000, "time": 0}
	last_fetch = Utils.get_state_data("season_list")
	if last_fetch.max_time == 0:
		is_true = True
		while is_true:
			try:
				last_fetch = Utils.get_state_data("season_list")
				if last_fetch:
					params['id'] = int(last_fetch.max_id)
					params['limit'] = last_fetch.limit
				response = await get_season_list(params)
				if response['results']:
					for item in response['results']:
						await SeasonListJob.run(item)
					Utils.update_last_data(MatchListModel, 'season_list')
				else:
					is_true = False
			except Exception as e:
				logger.error(e)


async def init_stage_list():
	params = {"id": -1, "limit": 1000, "time": 0}
	last_fetch = Utils.get_state_data("stage_list")
	if last_fetch.max_time == 0:
		is_true = True
		while is_true:
			last_fetch = Utils.get_state_data("stage_list")
			try:
				params['id'] = last_fetch.max_id
				params['limit'] = last_fetch.limit
				response = await get_stage_list(params)
				if response['results']:
					for item in response['results']:
						await StageListJob.run(item)
					Utils.update_last_data(MatchListModel, 'stage_list')
				else:
					is_true = False
			except Exception as e:
				logger.error(e)


async def init_compesation_list():
	params = {"id": -1, "limit": 1000, "time": 0}
	last_fetch = Utils.get_state_data("compensation_list")
	if last_fetch.max_time == 0:
		is_true = True
		while is_true:
			last_fetch = Utils.get_state_data("compensation_list")
			params['id'] = int(last_fetch.max_id)
			try:
				response = await get_compensation_list(params)
				if response['results']:
					for item in response['results']:
						await CompensationListJob.run(item)
					Utils.update_last_data(MatchListModel, 'compensation_list')
				else:
					is_true = False
			except Exception as e:
				logger.error(e)


async def init_country():
	await CountryJob.run()


async def init_match_analysis():
	await MatchAnalysisJob.run()


async def init_category():
	await CategoryJob.run()

async def init_match_trend():
	# 获取前30天的比赛
	t = 60 * 60 * 24 * (30 - 1)
	today = date.today()
	dt = datetime.combine(today, datetime.min.time())
	now = int(dt.timestamp())

	session = None
	ids = []
	try:
		db = Database()
		session = db.get_session()

		# 分批查询，每次获取 batch_size 条记录
		ids = MatchListModel.get_30dyas_date_ids(session, now - t, time.time())
	except Exception as e:
		logger.error(f"Error fetching match trend data: {e}")
	finally:
		if session: session.close()

	queue = asyncio.Queue()
	for id_value in ids:
		queue.put_nowait(id_value)

	# 创建多个并发任务处理队列中的数据
	workers = [asyncio.create_task(__match_trend_worker(queue)) for _ in range(50)]  # 启动50个工作协程
	await queue.join()  # 等待所有任务完成

	# 停止工作协程
	for _ in workers:
		await queue.put(None)  # 向队列中放入结束信号
	await asyncio.gather(*workers)  # 等待所有工作协程完成


async def __match_trend_worker(queue):
	"""工作协程：从队列中获取数据并处理"""
	while True:
		match_id = await queue.get()  # 从队列中获取match_id
		print(match_id)
		if match_id is None:  # 使用None作为结束信号
			break
		await MatchTrendJob.run(match_id)
		queue.task_done()  # 标记该任务已完成

async def init_data():
	await init_category()
	await init_venue_list()
	await init_country()
	await init_compesation_list()
	await init_feree_list()
	await init_player_list()
	await init_season_list()
	await init_stage_list()
	await init_competition_list()
	await init_competition_rule()
	await init_coach_list()
	await init_team_list()
	await init_match_list()
	await init_honor_list()
	await init_match_analysis()
	await init_match_trend()
