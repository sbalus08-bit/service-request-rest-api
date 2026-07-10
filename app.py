from flask import Flask, jsonify
from database import get_service_request, create_database

# Run the database function from database.py to create an empty database. 
create_database()

# Initiate the new app using Flask.

app = Flask(__name__)

# Create the API endpoint

@app.route("/api/service-request/<int:request_id>")

def service_request(request_id):

	request = get_service_request(request_id)

	if request is None:
		return jsonify({"error": "Service request not found"}), 404

	return jsonify(request)

# The following code starts the server when the app is ran directly.
# IP is set to 0.0.0.0 to allow connections from outside of the computer.

	if __name__ == "__main__":
		app.run(host="0.0.0.0", port=5000)

