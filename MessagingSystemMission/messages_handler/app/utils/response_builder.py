from MessagingSystemMission.messages_handler.app.utils.constants import Constants


class ResponseBuilder:
    def __init__(self, status_code: int, status_desc: str, messages_content: list = []):
        self.__status_code = status_code
        self.__status_desc = status_desc
        self.__messages_content = messages_content

    def build_response(self):
        response = {
            Constants.STATUS_CODE: self.__status_code,
            Constants.STATUS_DESCRIPTION: self.__status_desc,
            Constants.MESSAGES_CONTENT: self.__messages_content

        }
        if not response.get(Constants.MESSAGES_CONTENT):
            response.pop(Constants.MESSAGES_CONTENT)
        return response

