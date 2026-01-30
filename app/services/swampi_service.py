import requests

BASE_URL = "https://swapi.dev/api"

def get_characters():
    # Busca personagens na swapi

    url = f"{BASE_URL}/people/"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()["results"]


def get_films():
    url = f"{BASE_URL}/films/"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()["results"]


def get_film_by_id(film_id):
    # Busca filmes na swapi pelo id

    url = f"{BASE_URL}/films/{film_id}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def get_characters_from_film(character_urls):
    # Busca personagens relacionados a filmes

    characters = []

    for url in character_urls:
        response = requests.get(url)
        response.raise_for_status()
        characters.append(response.json())

    return characters
