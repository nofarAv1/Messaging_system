import json
import requests
from typing import Optional
from MessagingSystemMission.logger.logger import logger
from MessagingSystemMission.messages_handler.app.utils.constants import Constants


def saving_user(data: dict) -> Optional[requests.models.Response]:
    """
    This function send a post request for db_api to insert new user
    :param data: A dictionary with users names
    """
    if not isinstance(data, dict):
        return None
    res = requests.post(url=Constants.INSERT_USER_URL, json=data)
    return res


def write_message(data: dict) -> int:
    """
    This function parse the message data, validate him and
    Sending request to saving data in db
    :param data:
    """
    if not isinstance(data, dict):
        return 0
    sender = data.get(Constants.SENDER)
    receiver = data.get(Constants.RECEIVER)
    message = data.get(Constants.MESSAGE)
    # Case of required fields dont filled
    if None in [sender, receiver, message]:
        logger.error("Get unfilled of required fields, can't saving message")
        return 1
    # Saving the user in DB
    res = saving_user(data)
    if res is not None and res.status_code == 200:
        res_message = requests.post(url=Constants.INSERT_MESSAGE_URL, json=data)
        if res is not None and res_message.status_code == 200:
            logger.info(f"Sending {sender} message to {receiver} successfully")
            return 2
        else:
            logger.error("Failed to insert message to db")
            return 3

    else:
        logger.error("Failed to insert user to db")
        return Constants.ERROR_OCCURRED_SEND_MESSAGE


def get_all_messages(user: str) -> list:
    """
    This function send a request for GetMessageApi and get all the message of the given user
    :param user: using for get all the messages of this user
    :return: If messages exist list of them else empty list
    """
    url_all_messages = Constants.GET_ALL_MESSAGES_URL + user
    res = requests.get(url=url_all_messages)
    if res is not None and res.status_code == 200:
        res_as_json = json.loads(res.text)
        return res_as_json[Constants.MESSAGES_CONTENT]
    else:
        return []


def get_all_unread_messages(user: str) -> list:
    """
    This function send a request to get all the unread messages of specific user
    :param user: using for get all the unread messages of this user
    :return:
    """
    url_all_unread_messages = Constants.GET_ALL_UNREAD_MESSAGE_URL + user
    res = requests.get(url=url_all_unread_messages)
    if res is not None and res.status_code == 200:
        res_as_json = json.loads(res.text)
        return res_as_json[Constants.MESSAGES_CONTENT]
    else:
        return []


def reading_message() -> list:
    """
    This function send a request to get the last message from all the messages that exist
    :return:
    """
    url = Constants.URL_READ_MESSAGE
    res = requests.get(url=url)
    if res is not None and res.status_code == 200:
        res_as_json = json.loads(res.text)
        return res_as_json[Constants.MESSAGES_CONTENT]
    else:
        return []


def deleting_message(user_id: str, owner: str) -> int:
    """
    This function send a request to delete the last messages by a specific user id
    :param user_id: A specific user id
    :param owner: If the user_id is a sender of the message or not
    :return:
    """
    url_for_delete = Constants.DELETE_MESSAGE + user_id + "/" + owner
    res = requests.get(url=url_for_delete)
    if res is not None and res.status_code == 200:
        return 0
    else:
        return 1


