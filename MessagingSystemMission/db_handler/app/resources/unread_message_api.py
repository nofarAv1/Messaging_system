from flask_restful import Resource
from MessagingSystemMission.db_handler.app.utils import api_utils
from MessagingSystemMission.db_handler.app.models.messages_model import db, User, Messages
from MessagingSystemMission.db_handler.app.utils.constants import Constants as DBConstants


class UnreadMessageApi(Resource):
    def get(self, user, read=0):
        """
        This function get all the message that unread by receiver
        :param user: Using for get his received messages
        :param read: default to 0 , mean unread yet
        :return: all the message that unread by receiver
        """
        messages_list = []
        receiver = User.query.filter_by(user=user).first()
        messages = Messages.query.filter_by(receiver_id=receiver.id, message_read=read).all()
        if messages is not None:
            for message in messages:
                messages_list += [api_utils.get_messages(message)]
            return {DBConstants.STATUS: DBConstants.SUCCESS,
                    DBConstants.MESSAGES_CONTENT: messages_list}
        else:
            return None
