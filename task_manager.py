# task_manager.py
import logging
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger

from jobs.category_job import CategoryJob
from jobs.country_job import CountryJob
from jobs.match_analysis_job import MatchAnalysisJob


logger = logging.getLogger(__name__)

class TaskManager:
    def __init__(self):
        """初始化调度器"""
        self.scheduler = AsyncIOScheduler()

    def add_interval_task(self, job_id, task_func, interval_seconds, **kwargs):
        """添加一个基于时间间隔的任务"""
        logger.info(f"Adding task {job_id} with interval {interval_seconds} seconds.")
        self.scheduler.add_job(
            task_func,
            IntervalTrigger(seconds=interval_seconds),
            id=job_id,
            replace_existing=True,
            max_instances=1,
            **kwargs
        )

    def add_cron_task(self, job_id, task_func, cron_expression, **kwargs):
        """添加一个基于cron表达式的任务"""
        logger.info(f"Adding task {job_id} with cron expression {cron_expression}.")
        self.scheduler.add_job(
            task_func,
            CronTrigger.from_crontab(cron_expression),
            id=job_id,
            replace_existing=True,
            **kwargs
        )

    def shutdown(self):
        """关闭调度器"""
        if self.scheduler and self.scheduler.running:
            logger.info("Shutting down scheduler...")
            self.scheduler.shutdown(wait=False)
        else:
            logger.warning("Scheduler is not running or not initialized.")

    async def run(self):
        """注册所有的定时任务并启动调度器"""
        try:
            # 请求国家列表 每天00:00 一次
            self.add_cron_task("country", CountryJob.run, cron_expression="0 0 * * *")

            # 获取比赛分析数据每天06:00 13:00 各一次
            self.add_cron_task("match_analysis_12", MatchAnalysisJob.run, cron_expression="0 12 * * *")
            self.add_cron_task("match_analysis_15", MatchAnalysisJob.run, cron_expression="0 15 * * *")

            # 请求分类 每天00:00 一次
            self.add_cron_task("category", CategoryJob.run, cron_expression="0 0 * * *")

            self.scheduler.start()
            logger.info("Scheduler started successfully.")

            # 保持事件循环运行
            while True:
                await asyncio.sleep(1)
        except asyncio.CancelledError:
            # 处理任务被取消的情况
            logger.info("Tasks have been cancelled.")
            self.shutdown()
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            self.shutdown()