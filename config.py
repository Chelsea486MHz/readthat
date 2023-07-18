import os

TTS_LANGUAGE = 'en'

DATABASE_NAME = os.environ.get('DATABASE_NAME', 'db_name')
DATABASE_HOST = os.environ.get('DATABASE_HOST', 'db_host')
DATABASE_USER = os.environ.get('DATABASE_USER', 'db_username')
DATABASE_PASS = os.environ.get('DATABASE_PASS', 'db_password')

DATABASE_URI = 'mysql+pymysql://' + DATABASE_USER + ':' + DATABASE_PASS + '@' + DATABASE_HOST + '/' + DATABASE_NAME
