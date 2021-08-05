from sqlalchemy import desc
from flask_restful import Resource
from MessagingSystemMission.db_handler.app.models.messages_model import db, User, Messages
from MessagingSystemMission.db_handler.app.utils.constants import Constants as DBConstants


class DeleteMessageApi(Resource):
    # NOTE: For delete message i assumed that you mean to the last message from the given user.
    def get(self, user, owner):
        """
        This function delete message by the following order:
        1- Check if the user is the owner of the message
        2- Get the last message by the user
        3- Delete message
        :param user: Using for delete his message
        :param owner: Using for check if the user is a sender or a receiver
        :return:
        """
        if owner == "true":
            sender = User.query.filter_by(user=user).first()
            last_message = Messages.query.filter_by(sender_id=sender.id).order_by(desc('created_time')).first()
        else:
            receiver = User.query.filter_by(user=user).first()
            last_message = Messages.query.filter_by(receiver_id=receiver.id).order_by(desc('created_time')).first()
        if last_message is not None:
            db.session.delete(last_message)
            db.session.commit()
            return {DBConstants.STATUS: DBConstants.SUCCESS}
        else:
            return None
