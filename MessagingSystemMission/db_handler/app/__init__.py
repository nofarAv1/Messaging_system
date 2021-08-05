from flask import Flask
from flask_restful import Api
from MessagingSystemMission.db_handler.app.models.messages_model import db
from MessagingSystemMission.db_handler.app.resources.users_api import UsersApi
from MessagingSystemMission.db_handler.app.resources.messages_api import MessagesApi


def create_app():
    app = Flask(__name__)
    api = Api(app)

    # config and init the db
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db.init_app(app)

    # routes
    api.add_resource(UsersApi, "/db-api/insert_user/")
    api.add_resource(MessagesApi, "/db-api/insert_message/", "/db-api/all_messages/<string:user>")

    # drop old table and create new from modals
    with app.app_context():
        db.drop_all()
        db.create_all()

    return app
