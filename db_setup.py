from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
# from flask_bcrypt import Bcrypt
# from flask_mail import Mail
# from authlib.integrations.flask_client import OAuth
# from dp_store.config import Config


# oauth = OAuth()
db = SQLAlchemy()
# login_manager = LoginManager()
# login_manager.login_view = 'login'
# bcrypt = Bcrypt()
# mail = Mail()


def create_app():
    app = Flask(__name__)
    # app.config.from_object(Config)
    # app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///c:\\sqlite\\test.db"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # oauth.init_app(app)
    db.init_app(app)
    

    # from flaskauth.users.routes import users
    # from flaskauth.posts.routes import posts
    # from flaskauth.main.routes import main
    # from flaskauth.errors.handlers import errors

    # app.register_blueprint(users)
    # app.register_blueprint(posts)
    # app.register_blueprint(main)
    # app.register_blueprint(errors)
    
    return app

