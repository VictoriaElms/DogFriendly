from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "C:\\Users\\victo\\OneDrive\\Desktop\\CST 8333 Assignment\\DogFriendly\\dogfriendly.sqlite3"
# DB_NAME = "C:\\Users\\ElmsJ\\Desktop\\DogFriendly\\dogfriendly.sqlite3"


def config_blueprints(app):
    from routes.api import api
    from routes.auth import auth
    from routes.views import views

    app.register_blueprint(api, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(views, url_prefix="/")


def config_login_manager(app):
    from database.models import Users

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "hello key"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    config_blueprints(app)
    config_login_manager(app)

    return app