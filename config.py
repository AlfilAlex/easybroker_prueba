from os import path, getenv
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    BASE_URL = getenv('BASE_URL')
    PREFIX = getenv('PREFIX')

    TEMPLATES_AUTO_RELOAD = getenv('TEMPLATES_AUTO_RELOAD')
    FLASK_ENV = getenv('FLASK_ENV')
    DEBUG = getenv('DEBUG')

    EB_TOKEN = getenv('EB_TOKEN')
    EB_PROPERTY_PUBLIC_ID = getenv('EB_PROPERTY_PUBLIC_ID')
