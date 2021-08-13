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
            res_build = ResponseBuilder(200, Constants.GET_ALL_MESSAGES_SUCCESSFULLY, messages_list)
            session.pop("user", None)
        else:
            res_build = ResponseBuilder(401, Constants.REQUEST_TO_LOGIN + api.url_for(LoginApi))
        return jsonify(res_build.build_response())


class WriteApi(Resource):
    def post(self):
        post_args = parser.parse_args()
        res = message_server.write_message(post_args)
        if res == 0:
            res_build = ResponseBuilder(400, Constants.NOT_A_DATA_REQUIRED_FORMAT)
        elif res == 1:
            res_build = ResponseBuilder(400, Constants.UNFILLED_REQUIRED_FIELDS)
        elif res == 2:
            res_build = ResponseBuilder(200, Constants.MESSAGE_SENT_SUCCESSFULLY +
                                        f" to {post_args[Constants.RECEIVER]}")
        else:
            res_build = ResponseBuilder(500, Constants.ERROR_OCCURRED_SEND_MESSAGE)
        return jsonify(res_build.build_response())


class AllUnreadMessageApi(Resource):
    def get(self, user):
        if "user" in session:
            messages_list = message_server.get_all_unread_messages(user)
            res_build = ResponseBuilder(200, Constants.GET_ALL_UNREAD_MESSAGES_SUCCESSFULLY, messages_list)
            session.pop("user", None)
        else:
            res_build = ResponseBuilder(401, Constants.REQUEST_TO_LOGIN + api.url_for(LoginApi))
        return jsonify(res_build.build_response())


class ReadMessageApi(Resource):
    def get(self):
        messages_list = message_server.reading_message()
        res_build = ResponseBuilder(200, Constants.GET_LAST_MESSAGE_SUCCESSFULLY, messages_list)
        return jsonify(res_build.build_response())


class DeleteMessageApi(Resource):
    def get(self, user, owner):
        res = message_server.deleting_message(user, owner)
        if res == 0:
            res_build = ResponseBuilder(200, Constants.MESSAGE_DELETE_SUCCESSFULLY)
        else:
            res_build = ResponseBuilder(500, Constants.FAILED_DELETE_MESSAGE)
        return jsonify(res_build.build_response())


# Config Routes
api.add_resource(LoginApi, "/message-system/login")
api.add_resource(WriteApi, "/message-system/new_message")
api.add_resource(GetAllMessageApi, "/message-system/all_messages/<string:user>")
api.add_resource(AllUnreadMessageApi, "/message-system/all_unread_messages/<string:user>")
api.add_resource(ReadMessageApi, "/message-system/reading_message/")
api.add_resource(DeleteMessageApi, "/message-system/delete_message/<string:user>/<string:owner>")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)



