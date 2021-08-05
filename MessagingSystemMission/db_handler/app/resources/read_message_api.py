from flask_restful import Resource
from sqlalchemy import desc
from MessagingSystemMission.db_handler.app.utils import api_utils
from MessagingSystemMission.db_handler.app.models.messages_model import db, User, Messages
from MessagingSystemMission.db_handler.app.utils.constants import Constants as DBConstants


class ReadMessageApi(Resource):
    # NOTE: For read message i assumed that you mean to the last message the user got.
    # Read message can filter by sender, subject, receiver and etc.
    def get(self):
        the_last_message_unread = Messages.query.order_by(desc('created_time')).first()
        message = api_utils.get_messages(the_last_message_unread)
        if not the_last_message_unread.message_read:
            the_last_message_unread.message_read = True
            db.session.commit()
        return {DBConstants.STATUS: DBConstants.SUCCESS,
                DBConstants.MESSAGES_CONTENT: message}