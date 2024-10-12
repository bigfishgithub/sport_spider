import logging
import time

from database import Database
from jobs.BaseJob import BaseJob
from api.football_apis import get_competition_table_detail
from models.competition_table_detail_model import CompetitionTableDetailModel
from models.competition_table_promotion_model import CompetitionTablePromotionModel

logger = logging.getLogger(__name__)


class CompetitionTableDetailJob(BaseJob):
	@classmethod
	async def run(cls, ids):
		competition_id = ids[0]
		response = await get_competition_table_detail({"id": competition_id})
		if not response:
			return

		if response['results']:
			data = response['results']
			if data['season_id'] == 0:
				return
			updated_at = int(time.time())
			if len(data['tables']) >= 0:
				db = Database()
				session = db.get_session()
				try:
					for promotion in data['promotions']:
						promotion = {
							"competition_id": competition_id,
							"season_id": data['season_id'],
							"promotion_id": promotion['id'],
							"name_zh": promotion['name_zh'],
							"name_en": promotion['name_en'],
							"name_zht": promotion['name_zht'],
							"color": promotion['color'],
							"updated_at": updated_at,
						}
						competition_table_promotion = CompetitionTablePromotionModel(**promotion)
						competition_table_promotion.insert(session)
				except Exception as e:
					logger.error(e)
				finally:
					session.close()

				db = Database()
				session = db.get_session()
				try:
					for competition_detail in data['tables']:
						for table_detail in competition_detail['rows']:
							table = {
								"competition_id": competition_id,
								"season_id": data['season_id'],
								"table_id": competition_detail['id'],
								"team_id": table_detail['team_id'],
								"conference": competition_detail['conference'],
								"group": competition_detail['group'],
								"stage_id": competition_detail['stage_id'],
								"promotion_id": table_detail['promotion_id'],
								"points": table_detail['points'],
								"position": table_detail['position'],
								"deduct_points": table_detail['deduct_points'],
								"note": table_detail['note'],
								"total": table_detail['total'],
								"won": table_detail['won'],
								"draw": table_detail['draw'],
								"loss": table_detail['loss'],
								"goals": table_detail['goals'],
								"goals_against": table_detail['goals_against'],
								"goal_diff": table_detail['goal_diff'],
								"home_points": table_detail['home_points'],
								"home_position": table_detail['home_position'],
								"home_total": table_detail['home_total'],
								"home_won": table_detail['home_won'],
								"home_draw": table_detail['home_draw'],
								"home_loss": table_detail['home_loss'],
								"home_goals": table_detail['home_goals'],
								"home_goals_against": table_detail['home_goals_against'],
								"home_goal_diff": table_detail['home_goal_diff'],
								"away_points": table_detail['away_points'],
								"away_position": table_detail['away_position'],
								"away_total": table_detail['away_total'],
								"away_won": table_detail['away_won'],
								"away_draw": table_detail['away_draw'],
								"away_loss": table_detail['away_loss'],
								"away_goals": table_detail['away_goals'],
								"away_goals_against": table_detail['away_goals_against'],
								"away_goal_diff": table_detail['away_goal_diff'],
								"updated_at": updated_at,
							}
							competition_table_promotion = CompetitionTableDetailModel(**table)
							competition_table_promotion.insert(session)
				except Exception as e:
					logger.error(e)
				finally:
					session.close()
