from flask import Flask, jsonify
from flask import session
from flask_restful import Resource, Api, reqparse
from MessagingSystemMission.messages_handler.app import message_server
from MessagingSystemMission.messages_handler.app.utils.constants import Constants
from MessagingSystemMission.messages_handler.app.utils.response_builder import ResponseBuilder

app = Flask(__name__)
api = Api(app)

# Config secret key for session
app.config['SECRET_KEY'] = '1qaz2wsx3edc'

# Init parser
parser = reqparse.RequestParser()
parser.add_argument(Constants.USER, type=str, help='Unique user of sender')
parser.add_argument(Constants.SENDER, type=str, help='Unique user of sender')
parser.add_argument(Constants.RECEIVER, type=str, help='Unique id of receiver')
parser.add_argument(Constants.SUBJECT, type=str, help='The subject of the message')
parser.add_argument(Constants.MESSAGE, type=str, help='The message content')


class LoginApi(Resource):
    def post(self):
        post_args = parser.parse_args()
        user = post_args[Constants.USER]
        if user:
            session["user"] = user
            res_build = ResponseBuilder(200, Constants.LOGIN_PASSED_SUCCESSFULLY)
        else:
            res_build = ResponseBuilder(401, Constants.FAILED_TO_LOGIN)
        return jsonify(res_build.build_response())


class GetAllMessageApi(Resource):
    def get(self, user):
        if "user" in session:
            messages_list = message_server.get_all_messages(user)
            res_build = ResponseBuilder(200, Constants.GET_ALL_MESSAGES, messages_list)
            return jsonify(res_build)
        else:
            res_build = ResponseBuilder(401, Constants.REQUEST_TO_LOGIN + api.url_for(LoginApi))
            return res_build


class WriteApi(Resource):
    def post(self):
        post_args = parser.parse_args()
        return message_server.write_message(post_args)


class AllUnreadMessageApi(Resource):
    def get(self, user):
        if "user" in session:
            return message_server.get_all_unread_messages(user)
        else:
            return {Constants.RESPONSE: "Please login first in: " + api.url_for(LoginApi)}


class ReadMessageApi(Resource):
    def get(self):
        return message_server.reading_message()


class DeleteMessageApi(Resource):
    def get(self, user, owner):
        return message_server.deleting_message(user, owner)


# Config Routes
api.add_resource(LoginApi, "/message-system/login")
api.add_resource(WriteApi, "/message-system/new_message")
api.add_resource(GetAllMessageApi, "/message-system/all_message/<string:user>")
api.add_resource(AllUnreadMessageApi, "/message-system/all_unread_messages/<string:user>")
api.add_resource(ReadMessageApi, "/message-system/reading_message/")
api.add_resource(DeleteMessageApi, "/message-system/delete_message/<string:user>/<string:owner>")


if __name__ == '__main__':
    app.run(debug=True, port=5001)
    session.pop("user", None)

