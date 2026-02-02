import requests

BASE_URL = "https://swapi.dev/api"


def fetch(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def get_resource(resource):
    url = f"{BASE_URL}/{resource}/"
    return fetch(url)["results"]


def get_film_by_id(film_id):
    url = f"{BASE_URL}/films/{film_id}/"
    return fetch(url)


def get_resources_from_urls(urls):
    return [fetch(url) for url in urls]

