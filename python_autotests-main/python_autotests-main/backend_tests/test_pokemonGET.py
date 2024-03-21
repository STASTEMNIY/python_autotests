import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json'}

def test_get_creat_pokemon():
    """
    KTI-1 Get trainers by level
    """
    response = requests.get(url=f'{URL}/trainers', params={'level': 1}, timeout=5)
    assert response.status_code == 200, 'Unexpected statys code'