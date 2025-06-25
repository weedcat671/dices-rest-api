import flask
import json

from app import utils

app = flask.Flask(__name__)

@app.route("/roll", methods=["POST"])
def roll():
	try:
		request_data = flask.request.get_json()
		status, response_data = utils.make_roll_response(request_data)
		response = flask.make_response(json.dumps(response_data), status)
		return response
	except Exception as e:
		return json.dumps({"error": "Internal Server Error"}), 500
		