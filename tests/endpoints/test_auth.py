import os
import pytest


def test_auth_missing_api_key(client, monkeypatch):
    monkeypatch.setenv("API_KEY", "abc123")

    response = client.get("/films/1/characters")

    assert response.status_code == 401
    assert "Unauthorized" in response.get_json()["error"]


def test_auth_invalid_api_key(client, monkeypatch):
    monkeypatch.setenv("API_KEY", "abc123")

    response = client.get(
        "/films/1/characters",
        headers={"X-API-KEY": "wrong-key"}
    )

    assert response.status_code == 401
    assert "Unauthorized" in response.get_json()["error"]


def test_auth_valid_api_key(client, monkeypatch):
    monkeypatch.setenv("API_KEY", "abc123")

    response = client.get(
        "/films",
        headers={"X-API-KEY": "abc123"}
    )

    assert response.status_code == 200


def test_auth_api_key_not_configured(client, monkeypatch):
    monkeypatch.delenv("API_KEY", raising=False)

    response = client.get(
        "/films/1/characters",
        headers={"X-API-KEY": "abc123"}
    )

    assert response.status_code == 500
    assert "API key not configured" in response.get_json()["error"]
