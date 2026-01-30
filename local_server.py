from flask import Flask, request
from app.main import main

app = Flask(__name__)

@app.route("/", methods=["GET"])
@app.route("/characters", methods=["GET"])
def handle():
    return main(request)

if __name__ == "__main__":
    app.run(debug=True)
