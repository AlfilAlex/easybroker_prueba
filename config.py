from os import path, getenv
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    BASE_URL = getenv('BASE_URL')
    DEBUG = getenv('DEBUG')
    PREFIX = getenv('PREFIX')

    EB_TOKEN = getenv('EB_TOKEN')
    FLASK_ENV = getenv('FLASK_ENV')
    TEMPLATES_AUTO_RELOAD = getenv('TEMPLATES_AUTO_RELOAD')
