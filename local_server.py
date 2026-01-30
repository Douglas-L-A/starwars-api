from flask import Flask, request
from app.main import main

app = Flask(__name__)

@app.route("/", defaults={"path": ""}, methods=["GET"])
@app.route("/<path:path>", methods=["GET"])
def handler(path):
    return main(request)


if __name__ == "__main__":
    app.run(debug=True)
