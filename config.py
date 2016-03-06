import os
basedir = os.path.abspath(os.path.dirname(__file__))

user = "SOMEUSER"
database = "SOMEDATABASE"
server = "SOMESERVER"
password = "SOMEPASSWORD"


class Config:
    SECRET_KEY = "sOmEsEcReTkEy"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{0}:{1}@{2}/{3}'.format(user, password, server, database)


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(os.path.join(basedir, "base.db"))

config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}

