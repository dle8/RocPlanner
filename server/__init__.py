from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from celery import Celery
from config import config
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect

application = Flask(__name__, template_folder='../templates', static_url_path='', static_folder='../static')
application.config.from_object(config)

csrf = CSRFProtect(application)

# Initialize Flask Login Manager
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(application)

# Initialize Flask Cors
CORS(application)

# Initialize Celery
celery = Celery(application.name, broker=application.config['CELERY_BROKER_URL'])
celery.conf.update(application.config)

# Initialize Flask Mail
mail = Mail()
mail.init_app(application)


def _register_subpackages():
    import controllers
    import models


# Initialize SQL Alchemy
db = SQLAlchemy()
db.init_app(application)
_register_subpackages()
db.create_all(app=application)
