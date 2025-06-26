from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def hello_world():
    data = request.get_json()
    name = data.get("name")
    return f"<p>Hello, World! {name}</p>"

