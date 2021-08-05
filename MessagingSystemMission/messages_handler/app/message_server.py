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
    # Cast of required fields dont filled
    if None in [sender, receiver, message]:
        logger.error("Get unfilled of required fields, can't saving message")
        return {Constants.RESPONSE: Constants.UNFILLED_REQUIRED_FIELDS}
    # Saving the user in DB
    res = saving_user(data)
    if res.status_code == 200:
        res_message = requests.post(url=Constants.INSERT_MESSAGE_URL, json=data)
        if res_message.status_code == 200:
            logger.info(f"Sending {sender} message to {receiver} successfully")
            return {Constants.RESPONSE: Constants.MESSAGE_SENT_SUCCESSFULLY + f" to {receiver}"}
        else:
            logger.error("Failed to insert message to db")
            return {Constants.RESPONSE: Constants.ERROR_OCCURRED}

    else:
        logger.error("Failed to insert user to db")
        return {Constants.RESPONSE: Constants.ERROR_OCCURRED}


def get_all_messages(sender: str) -> dict:
    url_all_messages = Constants.GET_ALL_MESSAGES + sender
    res = requests.get(url=url_all_messages)
    if res.status_code == 200:
        res_as_json = json.loads(res.text)
        return {Constants.RESPONSE: res_as_json[Constants.MESSAGES_CONTENT]}
    else:
        return {Constants.RESPONSE: Constants.FAILED_GET_ALL_MESSAGE}


def get_all_unread_messages(data: dict) -> dict:
    raise NotImplementedError


def reading_message(data: dict) -> dict:
    raise NotImplementedError


def deleting_message(data: dict) -> dict:
    raise NotImplementedError


