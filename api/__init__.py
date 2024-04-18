from flask import Flask, request, jsonify
from flask_cors import CORS
from api.messagehandle.memoshandel import push_to_app1,push_to_app2

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.is_json:
        data = request.get_json()
        # print("Received data:", data)
        push_to_app1(data)  # Example of pushing to app1
        # Optionally uncomment to push to other apps
        push_to_app2(data)
        # push_to_app3(data)
        return jsonify({"status": "success", "data_received": data}), 200
    else:
        return jsonify({"status": "error", "message": "Request body must be JSON"}), 400

@app.route('/')
def hello_world():
    return 'Hello World!'


