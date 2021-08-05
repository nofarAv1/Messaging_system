class Constants:
    # FIELDS OF MESSAGES
    SENDER = "sender"
    RECEIVER = "receiver"
    SUBJECT = "subject"
    MESSAGE = "message"
    CREATION_DATE = "creation_date"

    # RESPONSE FIELDS
    RESPONSE = "Response"

    # TYPES OF RESPONSES
    EMPTY_DATA = "Message don't sent, empty data"
    UNFILLED_REQUIRED_FIELDS = "Message don't send, required fields are not filled"
    MESSAGE_SENT_SUCCESSFULLY_WITHOUT_SUBJECT = "Message sent successfully without subject"
    MESSAGE_SENT_SUCCESSFULLY = "Message sent successfully"
    ERROR_OCCURRED = "Can't sent message. Try again later"
    FAILED_GET_ALL_MESSAGE = "Failed to get all messages, Try again later"
    FAILED_GET_UNREAD_MESSAGES = "Failed to get unread messages, Try again later"
    FAILED_DELETE_MESSAGE = "Failed to delete messages, Try again later"
    MESSAGE_DELETE_SUCCESSFULLY = "Message delete successfully"
    SUCCESS = "SUCCESS"
    SENDER_ID = "Sender_id"
    RECEIVER_ID = "Receiver_id"
    MESSAGES_CONTENT = "Messages"

    # URLS:
    INSERT_USER_URL = "http://localhost:5000/db-api/insert_user/"
    INSERT_MESSAGE_URL = "http://localhost:5000/db-api/insert_message/"
    GET_ALL_MESSAGES = "http://localhost:5000/db-api/all_messages/"
    GET_ALL_UNREAD_MESSAGE = "http://localhost:5000/db-api/unread_messages/"
    URL_READ_MESSAGE = "http://localhost:5000/db-api/read_message/"
    DELETE_MESSAGE = "http://localhost:5000/db-api/delete_message/"



