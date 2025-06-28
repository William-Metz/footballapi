"""
Import statments import other people's code that make it easier
to do cool complex things!
"""
from flask import Flask, request, jsonify

"""
This is where our app's Flask instances is constructed
"""
app = Flask(__name__)

"""
This is where our base endpoint is declared.
It handles both GET and POST requests:
- GET: Accepts a 'name' parameter from the URL query string (e.g. /?name=Will)
- POST: Accepts a JSON payload with a 'name' key (e.g. {"name": "Will"})
Returns a personalized greeting in HTML format.
"""
@app.route("/", methods=["POST", "GET"])
def hello():
    if request.method == "POST":
        data = request.get_json()
        name = data.get("name")
    else:
        name = request.args.get("name", "Guest")
    return f"<p>Hello {name}!</p>"
