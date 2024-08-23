from flask import Flask, request, jsonify

app = Flask(__name__)

# Predefined valid user_id
VALID_USER_ID = "12345"

@app.route("/get-user/<user_id>")
def get_user(user_id):
    # Check if the provided user_id matches the valid user_id

    # If the user_id is valid, return the user data
    user_data = {
        "user_id": 12345,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

# *********************************************
# Check using POSTMAN
@app.route("/create", methods=["POST"])
def create_user():
    data = request.get_json()
    return jsonify(data), 200
# *********************************************

if __name__ == "__main__":
    app.run(debug=True)
