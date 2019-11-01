class Config(object):
    DEBUG = False

    # SQL Alchemy
    SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:Adu230999@localhost:3306/rocplanner'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Celery
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

    # Google mail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    MAIL_DEFAULT_SENDER = 'letuandung492@gmail.com'

    # Flask
    SECRET_KEY = 'secret'


config = Config()