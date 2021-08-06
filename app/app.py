# This is a sample Python script.

from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    # Use a breakpoint in the code line below to debug your script.
    return jsonify({'ip': request.remote_addr}), 200


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9000)