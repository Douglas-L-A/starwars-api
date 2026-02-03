def test_not_found(client):
    response = client.get("/error")

    assert response.status_code == 404

    data = response.get_json()
    assert "error" in data
