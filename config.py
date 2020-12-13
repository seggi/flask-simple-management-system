import os

basedir =  os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLAKCHEMY_COMMIT_ON_TEARDOWN = True 
    FLASK_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASK_MAIL_SENDER = 'Flasky Admin <nankim45@gmail.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod 
    def init_app(app):
        pass 

class DevelopmentConfig(Config):
    # DEBUG = True 
    # MAIL_SERVER = 'smtp.google.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True 
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'nk-account.sqlite')

    # SQLALCHEMY_DATABASE_URI = "mysql://root:@127.0.0.1/nk-accountability"
    SQLALCHEMY_DATABASE_URI = "mysql://root:@127.0.0.1/nk-account" 

    MYSQL_DATABASE_HOST = 'localhost'
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = ''
    MYSQL_DATABASE_DB = 'nk-account'
    

class TestingConfig(Config):
    TESTING = True 
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'nk-account.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'nk-account.sqlite')


config = {
    'development': DevelopmentConfig, 
    'testing': TestingConfig, 
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
