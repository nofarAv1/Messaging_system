import requests
from MessagingSystemMission.app.constants import Constants
from MessagingSystemMission.app.logger.logger import logger


def write_message(data: dict) -> dict:
    # Case of empty data
    if not data:
        logger.error("Get empty data, can't parse message")
        return {Constants.RESPONSE: Constants.EMPTY_DATA}
    sender = data.get(Constants.SENDER)
    receiver = data.get(Constants.RECEIVER)
    message = data.get(Constants.MESSAGE)
    subject = data.get(Constants.SUBJECT)
    # Cast of required fields dont filled
    if None in [sender, receiver, message]:
        logger.error("Get unfilled of required fields, can't saving message")
        return {Constants.RESPONSE: Constants.UNFILLED_REQUIRED_FIELDS}
    # Case of empty subject
    if "" == subject:
        logger.info(f"Sending {sender} message to {receiver} successfully")
        return {Constants.RESPONSE: Constants.MESSAGE_SENT_SUCCESSFULLY_WITHOUT_SUBJECT}
    # Saving the email in DB
    res = requests.post(url=Constants.UPDATE_URL, json=data)
    if res.status_code == 200:
        logger.info(f"Sending {sender} message to {receiver} successfully")
        return {Constants.RESPONSE: Constants.MESSAGE_SENT_SUCCESSFULLY + f" to {receiver}"}
    else:
        logger.error("Failed to insert email to db")
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


