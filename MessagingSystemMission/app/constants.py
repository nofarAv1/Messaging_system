class Constants:
    # FIELDS OF MESSAGES
    SENDER = "Sender"
    RECEIVER = "Receiver"
    SUBJECT = "Subject"
    MESSAGE = "Message"
    CREATION_DATE = "Creation_date"

    # RESPONSE FIELDS
    RESPONSE = "Response"

    # TYPES OF RESPONSES
    EMPTY_DATA = "Message don't sent, empty data"
    UNFILLED_REQUIRED_FIELDS = "Message don't send, required fields are not filled"
    MESSAGE_SENT_SUCCESSFULLY_WITHOUT_SUBJECT = "Message sent successfully without subject"
    MESSAGE_SENT_SUCCESSFULLY = "Message sent successfully"
    ERROR_OCCURRED = "Can't sent message. Try again later"
    SUCCESS = "SUCCESS"

    # URLS:
    UPDATE_URL = "http://localhost:5000/db-api/insert/"


