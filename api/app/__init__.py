from flask import Flask
from flask_admin import Admin
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from api.config import Config

db = SQLAlchemy()
migrate = Migrate()
admin = Admin(name="VR-Bike-App")


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)
    _register_blueprints(app)
    _populate_admin(admin)
    return app


def _register_blueprints(app):
    from api.app.main import bp as main_bp

    app.register_blueprint(main_bp)


def _populate_admin(admin):
    return


from api.app import models

if __name__ == "__main__":
    create_app()
