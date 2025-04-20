from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from .config import Settings

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Settings)

    db.init_app(app)
    ma.init_app(app)

    from .views import api_blueprint
    app.register_blueprint(api_blueprint)

    return app
