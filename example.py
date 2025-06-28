from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def hello():
    if request.method == "POST":
        data = request.get_json()
        name = data.get("name")
    else:
        name = request.args.get("name", "Guest")
    return f"<p>Hello {name}!</p>"
