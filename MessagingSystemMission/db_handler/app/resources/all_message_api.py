from flask_restful import Resource
from MessagingSystemMission.db_handler.app.utils import api_utils
from MessagingSystemMission.db_handler.app.models.messages_model import db, User, Messages
from MessagingSystemMission.db_handler.app.utils.constants import Constants as DBConstants


class GetMessageApi(Resource):
    def get(self, user):
        """
        This message get a user and return all the messages the user received
        :param user: Using for get his message
        :return: The messages the user received
        """
        messages_list = []
        receiver = User.query.filter_by(user=user).first()
        messages = Messages.query.filter_by(receiver_id=receiver.id).all()
        if messages is not None:
            for message in messages:
                messages_list += [api_utils.get_messages(message)]
            return {DBConstants.STATUS: DBConstants.SUCCESS,
                    DBConstants.MESSAGES_CONTENT: messages_list}
        else:
            return None
