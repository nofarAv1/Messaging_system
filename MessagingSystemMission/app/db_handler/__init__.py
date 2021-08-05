from flask import Flask
from flask_restful import Api
from MessagingSystemMission.app.db_handler.db_api import DBApi
from MessagingSystemMission.app.db_handler.messages_model import db


def create_app():
    app = Flask(__name__)
    api = Api(app)

    # config and init the db
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db.init_app(app)

    # routes
    api.add_resource(DBApi, "/db-api/insert/")

    # drop old table and create new from modals
    with app.app_context():
        db.drop_all()
        db.create_all()

    return app
