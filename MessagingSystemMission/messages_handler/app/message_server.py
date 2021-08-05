import json
import requests
from MessagingSystemMission.logger.logger import logger
from MessagingSystemMission.messages_handler.app.utils.constants import Constants


def saving_user(data: dict):
    res = requests.post(url=Constants.INSERT_USER_URL, json=data)
    return res


def write_message(data: dict) -> dict:
    sender = data.get(Constants.SENDER)
    receiver = data.get(Constants.RECEIVER)
    message = data.get(Constants.MESSAGE)
    subject = data.get(Constants.SUBJECT)
    # Cast of required fields dont filled
    if None in [sender, receiver, message]:
        logger.error("Get unfilled of required fields, can't saving message")
        return {Constants.RESPONSE: Constants.UNFILLED_REQUIRED_FIELDS}
    # Saving the user in DB
    res = saving_user(data)
    if res.status_code == 200:
        # Build data for saving message
        res_as_json = json.loads(res.text)
        message_data = {
            Constants.SENDER_ID: res_as_json.get(Constants.SENDER_ID),
            Constants.RECEIVER_ID: res_as_json.get(Constants.RECEIVER_ID),
            Constants.SUBJECT: subject,
            Constants.MESSAGE: message
        }
        res_message = requests.post(url=Constants.INSERT_MESSAGE_URL, json=message_data)
        if res_message.status_code == 200:
            logger.info(f"Sending {sender} message to {receiver} successfully")
            return {Constants.RESPONSE: Constants.MESSAGE_SENT_SUCCESSFULLY + f" to {receiver}"}
        else:
            logger.error("Failed to insert message to db")
            return {Constants.RESPONSE: Constants.ERROR_OCCURRED}

    else:
        logger.error("Failed to insert user to db")
        return {Constants.RESPONSE: Constants.ERROR_OCCURRED}


def get_all_messages(data: dict) -> dict:
    # TODO: parse from db
    return {Constants.RESPONSE: "all messages"}


def get_all_unread_messages(data: dict) -> dict:
    raise NotImplementedError


def reading_message(data: dict) -> dict:
    raise NotImplementedError


def deleting_message(data: dict) -> dict:
    raise NotImplementedError


