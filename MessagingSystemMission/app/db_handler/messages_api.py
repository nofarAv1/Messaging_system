from flask_restful import Resource, reqparse
from MessagingSystemMission.app.constants import Constants
from MessagingSystemMission.app.db_handler.messages_model import db, Messages
from MessagingSystemMission.app.db_handler.constants import Constants as DBConstants


parser = reqparse.RequestParser()
parser.add_argument(DBConstants.SENDER_ID, type=str, help='Unique id of sender')
parser.add_argument(DBConstants.RECEIVER_ID, type=str, help='Unique id of receiver')
parser.add_argument(Constants.SUBJECT, type=str, help='The subject of the message')
parser.add_argument(Constants.MESSAGE, type=str, help='The message content')


class MessagesApi(Resource):
    def post(self):
        post_args = parser.parse_args()
        message = Messages(sender_id=post_args[DBConstants.SENDER_ID],
                           receiver_id=post_args[DBConstants.RECEIVER_ID],
                           message_subject=post_args[Constants.SUBJECT],
                           message=post_args[Constants.MESSAGE])
        db.session.add(message)
        db.session.commit()
        return {DBConstants.STATUS: DBConstants.SUCCESS}



