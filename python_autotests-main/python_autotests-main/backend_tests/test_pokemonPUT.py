import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json'}

def test_put_change_pokemon():
    """
    KTI-2. put change pokemon
    """
    response = requests.put(url=f'{URL}/pokemons', headers=HEADER, timeout=5)
    print(f'Статус код: {response.status_code}. Сообщение: {response.json()["message"]}')