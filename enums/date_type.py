from enum import Enum

class DateType(Enum):
	SINGLE_GAME_LINEUP = 2              # 单场阵容
	HIGHLIGHT_VIDEO = 3                 # 集锦录像
	MATCH_MAP = 5                       # 对阵图
	STANDINGS = 6                       # 积分榜
	SEASON_TEAM_PLAYER_STATISTICS = 7   # 赛季球队球员统计
	FIFA_MEN_RANKING = 8                # fifa men排名
	FIFA_WOMEN_RANKING = 9              # fifa women排名
	CLUB_RANKING = 10                   # 俱乐部排名
	EVENT_ANIMATION = 12                # 事件动图


