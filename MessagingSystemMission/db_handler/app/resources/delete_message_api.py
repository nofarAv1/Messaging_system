from sqlalchemy import desc
from flask_restful import Resource
from MessagingSystemMission.db_handler.app.utils import api_utils
from MessagingSystemMission.db_handler.app.models.messages_model import db, User, Messages
from MessagingSystemMission.db_handler.app.utils.constants import Constants as DBConstants


class DeleteMessageApi(Resource):
    # NOTE: For delete message i assumed that you mean to the last message from the given user.
    def get(self, user, owner):
        # First check if the user is the owner of the message
        # Then get all the last message by the user
        if owner == "true":
            sender = User.query.filter_by(user=user).first()
            last_message = Messages.query.filter_by(sender_id=sender.id).order_by(desc('created_time')).first()
        else:
            receiver = User.query.filter_by(user=user).first()
            last_message = Messages.query.filter_by(receiver_id=receiver.id).order_by(desc('created_time')).first()
        db.session.delete(last_message)
        db.session.commit()
        return {DBConstants.STATUS: DBConstants.SUCCESS}