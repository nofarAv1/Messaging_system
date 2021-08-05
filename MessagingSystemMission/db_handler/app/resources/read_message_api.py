from flask_restful import Resource
from sqlalchemy import desc
from MessagingSystemMission.db_handler.app.utils import api_utils
from MessagingSystemMission.db_handler.app.models.messages_model import db, Messages
from MessagingSystemMission.db_handler.app.utils.constants import Constants as DBConstants


class ReadMessageApi(Resource):
    # NOTE: For read message i assumed that you mean to the last message the user got.
    # Read message can filter by sender, subject, receiver and etc.
    def get(self):
        """
        This function read the last message from all the messages that exist
        and update in db that the message was read
        :return: the last message from all the messages that exist
        """
        the_last_message = Messages.query.order_by(desc('created_time')).first()
        if the_last_message is not None:
            message = api_utils.get_messages(the_last_message)
            if not the_last_message.message_read:
                the_last_message.message_read = True
                db.session.commit()
            return {DBConstants.STATUS: DBConstants.SUCCESS,
                    DBConstants.MESSAGES_CONTENT: message}
        else:
            return None
