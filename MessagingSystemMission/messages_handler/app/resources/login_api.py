from flask import session
from flask_restful import Resource, reqparse
from MessagingSystemMission.messages_handler.app import message_server
from MessagingSystemMission.messages_handler.app.utils.constants import Constants

parser = reqparse.RequestParser()
parser.add_argument(Constants.USER, type=str, help='Unique user of sender')


class LoginApi(Resource):
    def post(self):
        post_args = parser.parse_args()
        user = post_args[Constants.USER]
        if user:
            session["user"] = user
            return {Constants.RESPONSE: Constants.LOGIN_PASSED_SUCCESSFULLY}
        else:
            return {Constants.RESPONSE: Constants.FAILED_TO_LOGIN}

