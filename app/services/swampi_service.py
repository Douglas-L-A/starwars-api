import requests

SWAPI_BASE_URL = "https://swapi.dev/api"

def get_characters():
    # Busca personagens na swapi

    url = f"{SWAPI_BASE_URL}/people/"
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        raise Exception("Erro ao acessar a SWAMPI")
    
    data = response.json()
    return data.get("results", [])