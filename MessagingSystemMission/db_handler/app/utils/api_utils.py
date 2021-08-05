from MessagingSystemMission.db_handler.app.models.messages_model import Messages
from MessagingSystemMission.db_handler.app.utils.constants import Constants as DBConstants


def get_messages(message: Messages) -> dict:
    message_dict = []
    created_message = message.created_time
    subject = message.message_subject
    message_content = message.message
    sender = message.sender.user
    message_dict = {
        DBConstants.CREATED_TIME: str(created_message),
        DBConstants.SUBJECT: subject,
        DBConstants.MESSAGES_CONTENT: message_content,
        DBConstants.SENDER: sender
    }
    return message_dict

