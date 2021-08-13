# from flask import Flask
# from urllib import request
#
# app = Flask(__name__)
#
# @app.route("/")
# def home():
#     return "Welcome to Messages system"
#
# # flask 1 is messages_handler
# @app.route("/message/")
# @app.route("/message/<path:path>")
# def flask1(path=""):
#     return request.urlopen("http://localhost:5001/" + path).read()
#
# # flask2 is db_handler
# @app.route("/db/")
# @app.route("/db/<path:path>")
# def flask2(path=""):
#     return request.urlopen("http://localhost:5002/" + path).read()
#
#
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", debug=True, port=5000)