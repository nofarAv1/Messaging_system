from flask_restful import Resource, reqparse
from MessagingSystemMission.messages_handler.app import message_server


class ReadMessageApi(Resource):
    def get(self):
        return message_server.reading_message()
