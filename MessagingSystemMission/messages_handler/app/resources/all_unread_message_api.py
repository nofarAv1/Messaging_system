from flask_restful import Resource, reqparse
from MessagingSystemMission.messages_handler.app import message_server


class AllUnreadMessageApi(Resource):
    def get(self, user):
        return message_server.get_all_unread_messages(user)