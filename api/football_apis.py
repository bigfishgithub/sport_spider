from http_client import HttpClient

http_client = HttpClient()

async def get_language(params):
	"""获取多语言"""
	return await http_client.get('/api/v5/football/language/list',params=params)

async def get_category():
	"""获取分类列表"""
	return await http_client.get('/api/v5/football/category/list')

async def get_coach(params):
	"""获取教练列表"""
	return await http_client.get('/api/v5/football/coach/list',params)

async def get_compensation_list(params):
	"""获取比赛历史同赔统计列表"""
	return await http_client.get('/api/v5/football/compensation/list',params)

async def get_competition_list(params):
	"""获取比赛列表"""
	return await http_client.get('/api/v5/football/competition/list',params)

async def get_country_list():
	"""获取国家列表"""
	return await http_client.get('/api/v5/football/country/list')

async def get_competition_rule_list(params):
	"""获取赛事赛制列表"""
	return await http_client.get('/api/v5/football/competition/rule/list',params)

async def get_team_list(params):
	"""获取球队列表"""
	return await http_client.get('/api/v5/football/team/list',params)

async def get_player_list(params):
	"""获取球员列表"""
	return await http_client.get('/api/v5/football/player/list',params)

async def get_referee_list(params):
	"""获取裁判列表"""
	return await http_client.get('/api/v5/football/referee/list',params)

async def get_venue_list(params):
	"""获取场馆列表"""
	return await http_client.get('/api/v5/football/venue/list',params)

async def get_honor_list(params):
	"""获取荣誉列表"""
	return await http_client.get('/api/v5/football/honor/list',params)

async def get_season_list(params):
	"""获取赛季列表"""
	return await http_client.get('/api/v5/football/season/list',params)

async def get_stage_list(params):
	"""获取阶段列表"""
	return await http_client.get('/api/v5/football/stage/list',params)

async def get_more_update():
	"""获取更新数据"""
	return await http_client.get('/api/v5/football/data/more/update')

async def get_match_list(params):
	"""获取比赛列表"""
	return await http_client.get('/api/v5/football/recent/match/list',params)

async def get_match_analysis(params):
	"""获取比赛列表"""
	return await http_client.get('/api/v5/football/match/analysis',params)

async def get_match_live_update():
	"""获取历史比赛球队统计数据"""
	return await http_client.get('/api/v5/football/match/live')

async def get_match_live(params):
	"""获取历史比赛统计数据"""
	return await http_client.get('/api/v5/football/match/live/history',params)

async def get_match_trend(params):
	"""获取比赛趋势详情"""
	return await http_client.get('/api/v5/football/match/trend/detail',params)

async def get_match_lineup(params):
	"""获取比赛阵容详情"""
	return await http_client.get('/api/v5/football/match/lineup/detail',params)

async def get_team_stats_update():
	"""获取比赛球队统计列表"""
	return await http_client.get('/api/v5/football/match/team_stats/list')

async def get_player_stats_update():
	"""获取比赛球员统计列表"""
	return await http_client.get('/api/v5/football/match/player_stats/list')

async def get_player_stats(params):
	"""获取历史比赛球员统计数据"""
	return await http_client.get('/api/v5/football/match/player_stats/detail',params)

async def get_video_stream(params):
	"""获取版权比赛集锦录像地址"""
	return await http_client.get('/api/v5/football/match/stream/video_collection',params)

async def get_table_detail():
	"""获取实时积分榜数据"""
	return await http_client.get('/api/v5/football/table/live')

async def delete_data():
	"""获取实时积分榜数据"""
	return await http_client.get('/api/v5/football/table/live')

async def get_team_stats(params):
	"""获取历史比赛球队统计数据"""
	return await http_client.get('/api/v5/football/match/team_stats/list',params)

async def get_season_bracket(params):
	"""获取淘汰阶段对阵图数据"""
	return await http_client.get('/api/v5/football/season/bracket',params)

async def get_competition_table_detail(params):
	"""获取淘汰阶段对阵图数据"""
	return await http_client.get('/api/v5/football/competition/table/detail',params)

async def get_competition_stats(params):
	"""获取淘汰阶段对阵图数据"""
	return await http_client.get('/api/v5/football/competition/stats/detail',params)

async def get_deleted():
	"""获取删除数据"""
	return await http_client.get('/api/v5/football/deleted')

async def get_live_stream():
	"""获取版权比赛直播地址"""
	return await http_client.get('/api/v5/football/match/stream/urls_free')


















