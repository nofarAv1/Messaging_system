from flask_restful import Resource, reqparse
from MessagingSystemMission.db_handler.app.models.messages_model import db, User
from MessagingSystemMission.messages_handler.app.utils.constants import Constants
from MessagingSystemMission.db_handler.app.utils.constants import Constants as DBConstants


parser = reqparse.RequestParser()
parser.add_argument(Constants.SENDER, type=str, help='Unique user of sender')
parser.add_argument(Constants.RECEIVER, type=str, help='Unique user of receiver')


class UsersApi(Resource):
    def post(self):
        post_args = parser.parse_args()
        sender = User(user=post_args[Constants.SENDER])
        receiver = User(user=post_args[Constants.RECEIVER])
        sender_id = User.query.filter_by(user=sender.user).first()
        receiver_id = User.query.filter_by(user=receiver.user).first()
        if sender_id is None:
            db.session.add(sender)
            db.session.commit()
        if receiver_id is None:
            db.session.add(receiver)
            db.session.commit()
        return {DBConstants.STATUS: DBConstants.SUCCESS,
                DBConstants.SENDER_ID: sender.id,
                DBConstants.RECEIVER_ID: receiver.id}



