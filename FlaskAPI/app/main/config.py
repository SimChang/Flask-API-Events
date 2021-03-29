import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'd4ee0ca137bd4aab8fd67365fe485a05')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    MONGODB_SETTINGS = {
        'db': 'bioserenityDevDB',
        'host': 'localhost',
        'port': 27017
    }


class ProductionConfig(Config):
    DEBUG = False
    MONGODB_SETTINGS = {
        'db': 'bioserenityProdDB',
        'host': 'localhost',
        'port': 27017
    }


config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
