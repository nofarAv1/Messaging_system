from flask_restful import Resource, reqparse
from MessagingSystemMission.app.constants import Constants
from MessagingSystemMission.app.db_handler.messages_model import db, User, Messages
from MessagingSystemMission.app.db_handler.constants import Constants as DBConstants


parser = reqparse.RequestParser()
parser.add_argument(Constants.SENDER, type=str, help='Unique email of sender')
parser.add_argument(Constants.RECEIVER, type=str, help='Unique email of receiver')
parser.add_argument(Constants.SUBJECT, type=str, help='The subject of the message')
parser.add_argument(Constants.MESSAGE, type=str, help='The message content')


class DBApi(Resource):
    def post(self):
        post_args = parser.parse_args()
        sender = User(user=post_args[Constants.SENDER])
        receiver = User(user=post_args[Constants.RECEIVER])
        message = Messages(sender_id=sender.user,
                           receiver_id=receiver.user,
                           message_subject=post_args[Constants.SUBJECT],
                           message=post_args[Constants.MESSAGE])
        db.session.add(sender)
        db.session.add(receiver)
        db.session.add(message)
        db.session.commit()
        return {DBConstants.RESPONSE: DBConstants.SUCCESS}

