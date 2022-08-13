from os import path, getenv
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class BaseConfig:
    PREFIX = getenv('PREFIX')
    pass


class DevelopmentConfig(BaseConfig):
    TEMPLATES_AUTO_RELOAD = getenv('TEMPLATES_AUTO_RELOAD')
    FLASK_DEBUG = getenv('FLASK_DEBUG')

    EB_PROPERTY_PUBLIC_ID = getenv('EB_PROPERTY_PUBLIC_ID_DEVELOPMENT')
    EB_TOKEN = getenv('EB_TOKEN_DEVELOPMENT')
    EB_BASE_URL = getenv('EB_BASE_URL_DEVELOPMENT')


class ProductionConfig(DevelopmentConfig):
    TEMPLATES_AUTO_RELOAD = False
    FLASK_DEBUG = False

    EB_PROPERTY_PUBLIC_ID = getenv('EB_PROPERTY_PUBLIC_ID')
    EB_TOKEN = getenv('EB_TOKEN_PRODUCTION')
    EB_BASE_URL = ''


class TestingConfig(DevelopmentConfig):
    pass
