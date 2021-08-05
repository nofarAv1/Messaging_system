from flask_restful import Resource, reqparse
from MessagingSystemMission.messages_handler.app import message_server
from MessagingSystemMission.messages_handler.app.utils.constants import Constants

parser = reqparse.RequestParser()
parser.add_argument(Constants.SENDER, type=str, help='Unique user of sender')
parser.add_argument(Constants.RECEIVER, type=str, help='Unique id of receiver')
parser.add_argument(Constants.SUBJECT, type=str, help='The subject of the message')
parser.add_argument(Constants.MESSAGE, type=str, help='The message content')


class WriteApi(Resource):
    def post(self):
        post_args = parser.parse_args()
        return message_server.write_message(post_args)
