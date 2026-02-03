def test_list_films_success(client):
    response = client.get(
        "/films",
        headers={"X-API-KEY": "test-key"}
    )

    assert response.status_code == 200

    data = response.get_json()

    assert "count" in data
    assert "results" in data


def test_list_film_characters_success(client):
    response = client.get(
        "/films/1/characters",
        headers={"X-API-KEY": "test-key"}
    )

    assert response.status_code == 200

    data = response.get_json()

    assert "film" in data
    assert "characters" in data
    assert "total_characters" in data
