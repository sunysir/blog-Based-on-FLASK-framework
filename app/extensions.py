from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager
from flask import url_for
from flask_uploads import configure_uploads,IMAGES,patch_request_class,UploadSet
import pymysql
pymysql.install_as_MySQLdb()
bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
migrate = Migrate(db=db)
moment = Moment()
photos = UploadSet("photos", IMAGES)
login_manage = LoginManager()
def config_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app)
    moment.init_app(app)
    configure_uploads(app, photos)
    patch_request_class(app,size=None)
    login_manage.init_app(app)
    login_manage.login_view = "user.login"
    login_manage.login_message = '需要登录才能访问'
    login_manage.session_protection = 'strong'

