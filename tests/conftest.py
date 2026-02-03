import sys
import os
import pytest
from flask import Flask, request

# Garantir que o módulo app seja encontrado
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from app.main import main  # ajuste se o caminho for diferente


# Fixture do client
@pytest.fixture
def client():
    app = Flask(__name__)

    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def catch_all(path):
        response, status, headers = main(request)
        return response, status, headers

    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client
