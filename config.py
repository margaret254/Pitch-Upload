import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('pitch')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:maggie@localhost/pitch-upload'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    #simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    #email configuration
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Watchlist'
    SENDER_EMAIL = 'titusouko@gmail.com'

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:@Sopiti1221@localhost/pitch'

class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:@Sopiti1221@localhost/pitch'
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test': TestConfig
}