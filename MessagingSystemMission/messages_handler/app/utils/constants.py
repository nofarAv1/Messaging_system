class Constants:

    # LOGIN FIELDS
    USER = "user"
    # FIELDS OF MESSAGES
    SENDER = "sender"
    RECEIVER = "receiver"
    SUBJECT = "subject"
    MESSAGE = "message"
    CREATION_DATE = "creation_date"

    # RESPONSE FIELDS
    RESPONSE = "Response"
    STATUS_CODE = "status_code"
    STATUS_DESCRIPTION = "status_description"
    MESSAGE_CONTENT = "message_content"

    # TYPES OF RESPONSES
    REQUEST_TO_LOGIN = "Please Login first!"
    LOGIN_PASSED_SUCCESSFULLY = "Login passed successfully"
    FAILED_TO_LOGIN = "Failed to login"
    EMPTY_DATA = "Message don't sent, empty data"
    UNFILLED_REQUIRED_FIELDS = "Message don't send, required fields are not filled"
    MESSAGE_SENT_SUCCESSFULLY_WITHOUT_SUBJECT = "Message sent successfully without subject"
    MESSAGE_SENT_SUCCESSFULLY = "Message sent successfully"
    NOT_A_DATA_REQUIRED_FORMAT = "Not a required data format. Please send message in right format"
    ERROR_OCCURRED_SEND_MESSAGE = "Can't sent message. Try again later"
    FAILED_GET_ALL_MESSAGE = "Failed to get all messages, Try again later"
    FAILED_GET_UNREAD_MESSAGES = "Failed to get unread messages, Try again later"
    FAILED_DELETE_MESSAGE = "Failed to delete messages, Try again later"
    MESSAGE_DELETE_SUCCESSFULLY = "Message delete successfully"
    GET_ALL_MESSAGES_SUCCESSFULLY = "Get all messages successfully"
    GET_ALL_UNREAD_MESSAGES_SUCCESSFULLY = "Get all messages successfully"
    GET_LAST_MESSAGE_SUCCESSFULLY = "Get last message successfully"
    SUCCESS = "SUCCESS"
    SENDER_ID = "Sender_id"
    RECEIVER_ID = "Receiver_id"
    MESSAGES_CONTENT = "Messages"

    # URLS:
    INSERT_USER_URL = "http://localhost:5002/db-api/insert_user/"
    INSERT_MESSAGE_URL = "http://localhost:5002/db-api/insert_message/"
    GET_ALL_MESSAGES_URL = "http://localhost:5002/db-api/all_messages/"
    GET_ALL_UNREAD_MESSAGE_URL = "http://localhost:5002/db-api/unread_messages/"
    URL_READ_MESSAGE = "http://localhost:5002/db-api/read_message/"
    DELETE_MESSAGE = "http://localhost:5002/db-api/delete_message/"



