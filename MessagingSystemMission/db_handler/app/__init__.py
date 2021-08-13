from flask import Flask
from flask_restful import Api
from flask_session import Session
from MessagingSystemMission.db_handler.app.models.messages_model import db
from MessagingSystemMission.db_handler.app.resources.users_api import UsersApi
from MessagingSystemMission.db_handler.app.resources.all_message_api import GetMessageApi
from MessagingSystemMission.db_handler.app.resources.read_message_api import ReadMessageApi
from MessagingSystemMission.db_handler.app.resources.unread_message_api import UnreadMessageApi
from MessagingSystemMission.db_handler.app.resources.delete_message_api import DeleteMessageApi
from MessagingSystemMission.db_handler.app.resources.saving_messages_api import SavingMessageApi


def create_app():
    app = Flask(__name__)
    api = Api(app)
    # config and init the db
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db.init_app(app)

    # routes
    api.add_resource(UsersApi, "/db-api/insert_user/")
    api.add_resource(SavingMessageApi, "/db-api/insert_message/")
    api.add_resource(GetMessageApi, "/db-api/all_messages/<string:user>")
    api.add_resource(UnreadMessageApi, "/db-api/unread_messages/<string:user>")
    api.add_resource(ReadMessageApi, "/db-api/read_message/")
    api.add_resource(DeleteMessageApi, "/db-api/delete_message/<string:user>/<string:owner>")

    # drop old table and create new from modals
    with app.app_context():
        db.drop_all()
        db.create_all()

    return app
