from flask import Flask
from flask_restful import Api
from MessagingSystemMission.messages_handler.app.resources.write_message_api import WriteApi
from MessagingSystemMission.messages_handler.app.resources.get_all_message_api import GetAllMessageApi


def create_app():
    app = Flask(__name__)
    api = Api(app)

    # routes
    api.add_resource(WriteApi, "/message-system/new_message")
    api.add_resource(GetAllMessageApi, "/message-system/all_message/<string:user>")
    # api.add_resource(WriteApi, "/message-system/all_unread_messages/")
    # api.add_resource(WriteApi, "/message-system/reading_message/")
    # api.add_resource(WriteApi, "/message-system/delete_message/")

    return app
