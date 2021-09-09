import flask
import flask_sqlalchemy
from flask_login import LoginManager

db = flask_sqlalchemy.SQLAlchemy()

def create_app():
    app = flask.Flask(__name__)
    app.config['SECRET_KEY'] = 'heythere'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    manager = LoginManager()
    manager.init_app(app)

    from .models import User

    @manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    db.init_app(app)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
