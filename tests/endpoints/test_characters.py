def test_list_characters_success(client):
    response = client.get("/characters")

    assert response.status_code == 200

    data = response.get_json()

    assert "count" in data
    assert "results" in data
    assert isinstance(data["results"], list)


def test_list_characters_invalid_filter(client):
    response = client.get("/characters?banana=Luke")

    assert response.status_code == 400

    data = response.get_json()

    assert "error" in data
