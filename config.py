import os
from pathlib import Path
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

class Config:
	"""项目基础配置"""
	DEBUG = True

	DATABASE_URL            =   os.getenv('DATEBASE_URL')                   # 数据库连接地址
	LOGLEVEL                =   os.getenv('LOGLEVEL', 'DEBUG').upper()      # LOG日志级别
	LOG_DIR                 =   os.getenv('LOG_DIR', 'log')                 # LOG日志目录
	API_KEY                 =   os.getenv('API_KEY')# API 密钥
	SECRET_KEY              =   os.getenv('SECRET_KEY')                            # 用于加密和签名
	DATABASE_USER           =   os.getenv('DATABASE_USER')                         # 数据库账户
	DATABASE_PASSWORD       =   os.getenv('DATABASE_PASSWORD')                      # 数据库密码
	API_URL                 =   os.getenv('API_URL')
	DATABASE_ENGINE = f"mysql+pymysql://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASS')}@{os.getenv('DATABASE_ADDR')}:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}"
	LAST_FETCH_FILE_PATH    =   Path(__file__).parent.joinpath('last_fetch.json')
