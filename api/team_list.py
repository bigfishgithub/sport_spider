import logging

from api.football_apis import get_team_list
from jobs.BaseJob import BaseJob
from models.team_list_model import TeamListModel
from utils import Utils
from enums.language_type import LanguageType

logger = logging.getLogger(__name__)


async def team_list_fetch():
	params = {"id": -1, "limit": 0, "time": 0}
	last_fetch = Utils.get_state_data("team_list")
	params['time'] = last_fetch.max_time
	params['limit'] = last_fetch.limit
	response = await get_team_list(params)
	if response['results']:
		yield response['results']
