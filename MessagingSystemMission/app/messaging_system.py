from flask import Flask, request, jsonify
from MessagingSystemMission.app import message_server

app = Flask(__name__)


@app.route('/new_message', methods=["POST"])
def saving_message():
    data = request.json
    return jsonify(message_server.write_message(data))


@app.route('/all_messages', methods=["POST"])
def get_all_messages():
    data = request.json
    return jsonify(message_server.get_all_messages(data))


@app.route('/all_unread_messages', methods=["POST"])
def get_all_unread_messages():
    data = request.json
    return jsonify(message_server.get_all_messages(data))


@app.route('/reading_message', methods=["POST"])
def reading_message():
    data = request.json
    return jsonify(message_server.reading_message(data))


@app.route('/delete_message', methods=["POST"])
def deleting_message():
    data = request.json
    return jsonify(message_server.deleting_message(data))


if __name__ == '__main__':
    app.run(debug=True, port=5001)