from flask_restful import Resource
from MessagingSystemMission.messages_handler.app import message_server


class DeleteMessageApi(Resource):
    def get(self, user, owner):
        return message_server.deleting_message(user, owner)
