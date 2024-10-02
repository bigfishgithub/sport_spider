import logging
import os
from config import Config
from logging.handlers import RotatingFileHandler



class Logger:

	@staticmethod
	def setup_logging():
		"""配置日志记录"""

		# 确保日志目录存在
		os.makedirs(Config.LOG_DIR, exist_ok=True)

		# 创建日志格式
		debug_format = logging.Formatter(
			'%(asctime)s - %(levelname)s - %(message)s - %(filename)s:%(lineno)s',
			datefmt='%Y-%m-%d %H:%M:%S'
		)

		# 设置信息日志处理器
		info_handler = RotatingFileHandler(os.path.join(Config.LOG_DIR, "app.log"), maxBytes=10 * 1024 * 1024, backupCount=5, encoding='utf-8')
		info_handler.setFormatter(debug_format)

		# 获取 logger 对象
		logger = logging.getLogger()
		logger.setLevel(Config.LOGLEVEL)  # 设置全局日志级别

		# 添加处理器到 logger
		logger.addHandler(info_handler)

