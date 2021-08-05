from flask_restful import Resource, reqparse
from MessagingSystemMission.messages_handler.app.utils.constants import Constants
from MessagingSystemMission.db_handler.app.models.messages_model import db, User, Messages
from MessagingSystemMission.db_handler.app.utils.constants import Constants as DBConstants


parser = reqparse.RequestParser()
parser.add_argument(DBConstants.SENDER, type=str, help='Unique user of sender')
parser.add_argument(DBConstants.RECEIVER, type=str, help='Unique user of receiver')
parser.add_argument(Constants.SUBJECT, type=str, help='The subject of the message')
parser.add_argument(Constants.MESSAGE, type=str, help='The message content')


class SavingMessageApi(Resource):
    def post(self):
        post_args = parser.parse_args()
        sender = User.query.filter_by(user=post_args[DBConstants.SENDER]).first()
        receiver = User.query.filter_by(user=post_args[DBConstants.RECEIVER]).first()
        message = Messages(sender=sender,
                           receiver=receiver,
                           message_subject=post_args[Constants.SUBJECT],
                           message=post_args[Constants.MESSAGE])
        db.session.add(message)
        db.session.commit()
        return {DBConstants.STATUS: DBConstants.SUCCESS}






