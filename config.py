class Config(object):
    DEBUG = False

    # SQL Alchemy
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://administrator:Aa!1998123@localhost:3306/rocplanner'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Celery
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

    # Google mail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'rocplanner@gmail.com'
    MAIL_PASSWORD = 'zubwsajlkepnxpoj'
    MAIL_DEFAULT_SENDER = 'rocplanner@gmail.com'
    # zubwsajlkepnxpoj
    # Flask
    MAIL_APP_PASSWORDs = 'zubwsajlkepnxpoj'
    SECRET_KEY = 'secret'


config = Config()
